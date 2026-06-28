import requests
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

console = Console()
API_URL = "http://localhost:3000"

def gerenciar_categorias():
    console.print("\n[bold #00D7FF]─── Gerenciar Categorias ───[/bold #00D7FF]")
    acao = Prompt.ask("[#FFAF00]Opcoes:[/][1]Novo [2]Listar [3]Voltar", choices=["1", "2", "3"], show_choices=False)
    
    if acao == "1":
        nome = input("Nome da nova categoria: ")
        requests.post(f"{API_URL}/categorias", json={"nome": nome})
        console.print("[bold #50C878]Categoria criada com sucesso![/bold #50C878]")
    
    elif acao == "2":
        categorias = requests.get(f"{API_URL}/categorias").json()
        
        table = Table(title="Lista de Categorias", title_style="bold #8A2BE2", border_style="#8A2BE2")
        table.add_column("ID", style="#00D7FF", justify="center")
        table.add_column("Nome", style="#FFB6C1")
        
        for c in categorias:
            table.add_row(str(c.get("id")), c.get("nome"))
        console.print(table)