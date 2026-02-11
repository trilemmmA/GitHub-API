class GitHubUser:
    def __init__(self, user_id, login, url, score=None):
        self.user_id = user_id
        self.login = login
        self.url = url
        self.score = score
    
    def to_dict(self):
        return {
            "user_id": self.user_id,
            "login": self.login,
            "html_url": self.url,
            "score": self.score
        }
    
    def __str__(self):
        return f"User [{self.user_id} | {self.login} | {self.url} | {self.score}]"
    
    @property
    def profile(self):
        return f"https://github.com/{self.login}"
    
    @classmethod
    def from_api(cls, raw: dict):                
        return cls(
            raw.get("id"),
            raw.get("login"),
            raw.get("html_url"),
            raw.get("score")
        )
    
    def searchable(self):
        return [self.user_id, self.login, self.url, self.score]

    def enrich_w_details(self, client):                       
        try:
            detail_url = f"https://api.github.com/users/{self.login}"
            resp = client.session.get(detail_url)
            if resp.ok:
                data = resp.json()
                followers = data.get("followers", 0)
                repos = data.get("public_repos", 0)
                self.score = (followers + repos) / 2
                        
        except:
            self.score = 0
            
