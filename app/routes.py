from flask import render_template, jsonify, abort
from app import app, cache
from app.plex_client import PlexClient
import os

plex_server_url = os.getenv("PLEX_SERVER_URL", "http://localhost:32400")
plex_api_token = os.getenv("PLEX_API_TOKEN", "none")
dashboard_title = os.getenv("DASHBOARD_TITLE", "PlexSpot")
dashboard_icon = os.getenv("DASHBOARD_ICON", "https://cdn-icons-png.freepik.com/256/7664/7664156.png")

plex_client = PlexClient(plex_server_url, plex_api_token)

@app.route('/')
def index():
    libraries = get_libraries()
    default_library = libraries[0]['key'] if libraries else None
    return render_template('index.html', title=dashboard_title, icon=dashboard_icon, default_library=default_library)

@app.route('/api/user_stats')
@cache.cached(timeout=60)
def user_stats():
    try:
        stats = plex_client.get_user_stats()
        return jsonify(stats)
    except Exception as e:
        app.logger.error(f"Error in user_stats route: {str(e)}")
        return jsonify({'error': 'Unable to fetch user stats'}), 500

@app.route('/api/libraries')
@cache.cached(timeout=3600)
def get_libraries():
    library_stats = plex_client.get_library_stats()
    libraries = library_stats.get('MediaContainer', {}).get('Directory', [])
    if isinstance(libraries, dict):
        libraries = [libraries]
    return [{'key': lib['@key'], 'title': lib['@title']} for lib in libraries]

@app.route('/api/library_contents/<library_key>')
@cache.cached(timeout=3600)
def library_contents(library_key):
    contents = plex_client.get_library_contents(library_key)
    media_items = contents.get('MediaContainer', {}).get('Video', []) or contents.get('MediaContainer', {}).get('Directory', [])
    if isinstance(media_items, dict):
        media_items = [media_items]
    
    formatted_items = []
    for item in media_items:
        genres = item.get('Genre', [])
        if isinstance(genres, list):
            genres = ", ".join(genre.get('@tag', 'N/A') for genre in genres)
        elif isinstance(genres, dict):
            genres = genres.get('@tag', 'N/A')
        else:
            genres = 'N/A'
        
        formatted_items.append({
            "title": item.get('@title', 'N/A'),
            "year": item.get('@year', 'N/A'),
            "genres": genres
        })
    
    return jsonify(formatted_items)

@app.route('/api/genres/<library_key>')
@cache.cached(timeout=3600)
def get_genres(library_key):
    contents = plex_client.get_library_contents(library_key)
    media_items = contents.get('MediaContainer', {}).get('Video', []) or contents.get('MediaContainer', {}).get('Directory', [])
    
    all_genres = set()
    for item in media_items:
        genres = item.get('Genre', [])
        if isinstance(genres, list):
            all_genres.update(genre.get('@tag', 'N/A') for genre in genres)
        elif isinstance(genres, dict):
            all_genres.add(genres.get('@tag', 'N/A'))
    
    return jsonify(list(all_genres))
