import os
from flask import Flask
from flask_caching import Cache
from PIL import Image
import json
import requests
from io import BytesIO

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'
cache = Cache(app)

app.config['APP_VERSION'] = os.environ.get('APP_VERSION', 'local')
app.config['DASHBOARD_TITLE'] = os.environ.get('DASHBOARD_TITLE', 'PlexSpot')
app.config['DASHBOARD_ICON'] = os.environ.get('DASHBOARD_ICON', 'https://cdn-icons-png.freepik.com/256/7664/7664156.png')

def generate_icons():
    icon_url = app.config['DASHBOARD_ICON']
    sizes = [(192, 192), (512, 512)]
    icons = []

    try:
        if icon_url.startswith('http'):
            response = requests.get(icon_url)
            img = Image.open(BytesIO(response.content))
        else:
            img = Image.open(icon_url)

        for size in sizes:
            resized_img = img.resize(size)
            icon_filename = f"icon-{size[0]}x{size[1]}.png"
            icon_path = os.path.join(app.static_folder, icon_filename)
            resized_img.save(icon_path, 'PNG')
            icons.append({
                "src": f"/static/{icon_filename}",
                "sizes": f"{size[0]}x{size[1]}",
                "type": "image/png"
            })
    except Exception as e:
        app.logger.error(f"Error generating icons: {str(e)}")
        # Use default icon if there's an error
        icons = [
            {
                "src": "/static/default-icon.png",
                "sizes": "192x192",
                "type": "image/png"
            }
        ]

    return icons

def generate_manifest():
    manifest = {
        "name": app.config['DASHBOARD_TITLE'],
        "short_name": app.config['DASHBOARD_TITLE'],
        "start_url": "/",
        "display": "standalone",
        "background_color": "#ffffff",
        "theme_color": "#007bff",
        "icons": generate_icons()
    }

    manifest_path = os.path.join(app.static_folder, 'manifest.json')
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f)

generate_manifest()

from app import routes

