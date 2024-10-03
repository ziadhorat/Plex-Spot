import requests
import xmltodict
import logging
from urllib.parse import urljoin

logger = logging.getLogger(__name__)

class PlexClient:
    def __init__(self, base_url, token):
        self.base_url = base_url.rstrip('/')  # Remove trailing slash if present
        self.token = token
        self.headers = {
            "X-Plex-Token": self.token
        }

    def _make_request(self, endpoint):
        url = urljoin(self.base_url + '/', endpoint.lstrip('/'))
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"Error making request to {url}: {str(e)}")
            if isinstance(e, requests.exceptions.HTTPError):
                if e.response.status_code == 404:
                    logger.error(f"404 Error: The requested resource was not found. Please check your Plex server URL and ensure the endpoint exists.")
                elif e.response.status_code == 401:
                    logger.error("401 Error: Unauthorized. Please check your Plex API token.")
            raise

    def get_user_stats(self):
        try:
            response = self._make_request("/status/sessions")
            data = xmltodict.parse(response.text)
            media_container = data.get('MediaContainer', {})
            sessions = media_container.get('Video', [])
            
            if not isinstance(sessions, list):
                sessions = [sessions]
            
            active_sessions = len(sessions)
            users = {video['User']['@title'] for video in sessions if 'User' in video}
            total_users = len(users)
            
            return {
                'active_sessions': active_sessions,
                'total_users': total_users
            }
        except Exception as e:
            logger.error(f"Error getting user stats: {str(e)}")
            return {'active_sessions': 0, 'total_users': 0}

    def get_library_stats(self):
        try:
            response = self._make_request("/library/sections")
            return xmltodict.parse(response.text)
        except Exception as e:
            logger.error(f"Error getting library stats: {str(e)}")
            return {'MediaContainer': {'Directory': []}}

    def get_library_contents(self, library_key):
        try:
            response = self._make_request(f"/library/sections/{library_key}/all")
            return xmltodict.parse(response.text)
        except Exception as e:
            logger.error(f"Error getting library contents: {str(e)}")
            return {'MediaContainer': {'Video': []}}