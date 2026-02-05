from client import GitHubAPI
from storage import Storage
from app import App
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("GITHUB_TOKEN")

if not token:
    print("Token wasnt found in .env")
    exit(1)


def main():
    client = GitHubAPI("https://api.github.com/users", token=token)
    storage = Storage()
    app = App(client, storage)
    app.run()
    
if __name__ == "__main__":
    main()
