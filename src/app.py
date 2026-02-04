from analyzer import Analyzer

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.align import Align

class App:
    def __init__(self, client, storage):
        self.client = client
        self.storage = storage
        self.users = []
        self.last_result = None
        self.analyzer = Analyzer(self.users)
        self.console = Console()
    
    def load(self, limit):
        raw = self.client.fetch_users(limit)        
        self.users = list(self.analyzer.build_users(raw))
        
        self.analyzer = Analyzer(self.users)
            
    def search(self, pattern):
        
        result = self.analyzer.search(pattern)
        self.last_result = list(result)
        
        self.storage.save(self.last_result)    
    
    def show(self):
        if self.last_result is None:
            self.console.print("Search first", style="red", justify="center")
            return
        
        if not self.last_result:
            self.console.print("No matches found", style="bold green", justify="center")
            return
        
        table = Table(title="Result", header_style="bold magenta")
        
        table.add_column("ID", style="cyan")
        table.add_column("LOGIN", style="cyan red")
        table.add_column("URL", style="cyan green")
        table.add_column("SCORE", style="cyan blue")
        
        for user in self.last_result:
            table.add_row(
                str(user.user_id),
                user.login,
                user.url,
                str(user.score)
            )
        
        self.console.print(table)    
        
    def show_menu(self):
        text = """
    [bold cyan]1 - Load Users[/]
    [bold cyan]2 - Search[/]
    [bold cyan]3 - Show result[/]
    [bold cyan]4 - Exit[/]
    """
        self.console.print(
           Panel(Align.center(text), title="GitHub Analyzer", border_style="cyan") 
        )
    
    def run(self):
        self.show_menu()
        while True:            
            choice = input("Choose: ")
            
            if choice == "1":
                limit = input("How many users to load: ")
                
                if not limit.isdigit():
                    self.console.print("Enter number", style="bold red", justify="center")
                    continue
                
                self.load(int(limit))
                self.console.print(f"Loaded {len(self.users)} users", style="bold green", justify="center")
            
            elif choice == "2":
                if not self.users:
                    self.console.print("Load users first", style="bold red", justify="center")
                    continue
                
                pattern = input("Enter search pattern: ")               
                self.search(pattern)               
                self.show()               
            
            elif choice == "3":
                self.show()
            
            elif choice == "4":
                break
            
            else:
                self.console.print("Wrong command", style="bold red", justify="center")
                
