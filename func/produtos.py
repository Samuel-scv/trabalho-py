import requests
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

console = Console()
API_URL = "http://localhost:3000"

def gerenciar_produtos():
    console.print("\n[bold green]--- Gerenciar Produtos ---[/bold green]")
    acao = Prompt.ask("Opções: [1]Novo [2]Listar [3]Voltar", 
                      choices=["1", "2", "3"])
    
    if acao == "1":
        nome = input("Nome do Produto: ")
        preco = float(input("Preço: "))
        
        categorias = requests.get(f"{API_URL}/categorias").json()
        console.print("\n[bold]Categorias Disponíveis:[/bold]")
        ids_validos = []
        for c in categorias:
            console.print(f"ID: {c['id']} - {c['nome']}")
            ids_validos.append(str(c['id']))
            
        cat_id = Prompt.ask("\nEscolha o ID da Categoria do produto", choices=ids_validos)
        
        novo_produto = {"nome": nome, "preco": preco, "categoriaId": cat_id}
        requests.post(f"{API_URL}/produtos", json=novo_produto)
        console.print("[green]Produto cadastrado com sucesso![/green]")

    elif acao == "2":
        produtos = requests.get(f"{API_URL}/produtos").json()
        table = Table(title="Produtos")
        table.add_column("ID", style="cyan")
        table.add_column("Nome", style="magenta")
        table.add_column("Preço", style="green")
        table.add_column("ID Categoria", justify="right")
        for p in produtos:
            table.add_row(str(p.get("id")), p.get("nome"), f"R$ {p.get('preco'):.2f}", str(p.get("categoriaId")))
        console.print(table)