import requests
import xmltodict
import os
from app import cache

class PlexClient:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token
        self.headers = {
            "X-Plex-Token": self.token
        }

    @cache.cached(timeout=3600)
    def get_user_stats(self):
        url = f"{self.base_url}/status/sessions"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        
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

    @cache.cached(timeout=3600)
    def get_library_stats(self):
        url = f"{self.base_url}/library/sections"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return xmltodict.parse(response.text)

    @cache.cached(timeout=3600)
    def get_library_contents(self, library_key):
        url = f"{self.base_url}/library/sections/{library_key}/all"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return xmltodict.parse(response.text)

