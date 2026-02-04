import requests
from utils import call_log

class GitHubAPI:
    def __init__(self, url: str):
        self.url = url
    
    @call_log    
    def fetch_users(self, limit: int=30):
        params = {
            "per_page": limit
        }
        try:
            response = requests.get(self.url, timeout=10, params=params)        
            response.raise_for_status()
                
            return response.json()
        
        except requests.exceptions.Timeout:
            print("Timeout error")
        
        except requests.exceptions.ConnectionError:
            print("Connection error")
            
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e}")
            
        except requests.exceptions.RequestException as e:
            print(f"Request exception: {e}")
            
        return []
        