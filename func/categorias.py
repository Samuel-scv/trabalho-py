import requests
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

console = Console()
API_URL = "http://localhost:3000"

def gerenciar_categorias():
    console.print("\n[bold blue]--- Gerenciar Categorias ---[/bold blue]")
    acao = Prompt.ask("Opções: [1]Novo [2]Listar [3]Voltar", 
                      choices=["1", "2", "3"], show_choices=False)
    
    if acao == "1":
        nome = input("Nome da nova categoria: ")
        requests.post(f"{API_URL}/categorias", json={"nome": nome})
        console.print("[green]Categoria criada![/green]")
    
    elif acao == "2":
        categorias = requests.get(f"{API_URL}/categorias").json()
        table = Table(title="Categorias")
        table.add_column("ID", style="cyan")
        table.add_column("Nome", style="magenta")
        for c in categorias:
            table.add_row(str(c.get("id")), c.get("nome"))
        console.print(table)