from models import GitHubUser
import re
from utils import call_log
   
class Analyzer:
    def __init__(self, recieved_fields):
        self.recieved_fields = recieved_fields
    
    @call_log    
    def build_users(self, raw_list):
        for raw in raw_list:
            yield GitHubUser.from_api(raw)
    
    @call_log
    def search(self, pattern):
        regex = re.compile(pattern, re.I)
        
        for user in self.recieved_fields:
            for value in user.searchable():
                if regex.search(str(value)):
                    yield user
                    break
 