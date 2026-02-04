import json
from models import GitHubUser
from utils import call_log

class Storage:
    def __init__(self, filename="db/data_storage.json"):
        self.filename = filename
    
    @call_log    
    def save(self, data):
        prepared = []
        
        for user in data:
            prepared.append(user.to_dict())
        
        try:
            with open(self.filename, "w", encoding='utf-8') as f:
                json.dump(prepared, f, ensure_ascii=False, indent=4)
        
        except Exception as e:
            print(f"Save failed with: {e}")
    
    @call_log            
    def load(self):
        try:
            with open(self.filename, "r", encoding='utf-8') as f:
                data = json.load(f)
                
            users = []
            
            for raw in data:
                users.append(GitHubUser.from_api(raw))
                
            return users            
        
        except Exception as e:
            print(f"Load failed with: {e}")
            