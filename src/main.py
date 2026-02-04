from client import GitHubAPI
from storage import Storage
from app import App

def main():
    client = GitHubAPI("https://api.github.com/users")
    storage = Storage()
    app = App(client, storage)
    app.run()
    
if __name__ == "__main__":
    main()
