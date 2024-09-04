import requests
import xmltodict

class PlexClient:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token
        self.headers = {
            "X-Plex-Token": self.token
        }

    def get_user_stats(self):
        url = f"{self.base_url}/status/sessions"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        
        # Convert XML response to a Python dictionary
        return xmltodict.parse(response.text)

    def get_library_stats(self):
        url = f"{self.base_url}/library/sections"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        
        # Convert XML response to a Python dictionary
        return xmltodict.parse(response.text)
