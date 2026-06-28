import requests
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

console = Console()
API_URL = "http://localhost:3000"

def gerenciar_produtos():
    console.print("\n[bold #32CD32]─── Gerenciar Produtos ───[/bold #32CD32]")
    acao = Prompt.ask("[#FFAF00]Opcoes:[/][1]Novo [2]Listar [3]Voltar", choices=["1", "2", "3"])
    
    if acao == "1":
        nome = input("Nome do Produto: ")
        preco = float(input("Preco: "))
        
        categorias = requests.get(f"{API_URL}/categorias").json()
        console.print("\n[bold #8A2BE2]Categorias Disponiveis:[/bold #8A2BE2]")
        ids_validos = []
        for c in categorias:
            console.print(f"[#00D7FF]ID: {c['id']}[/] - [#FFB6C1]{c['nome']}[/]")
            ids_validos.append(str(c['id']))
            
        cat_id = Prompt.ask("\n[bold #FFAF00]Escolha o ID da Categoria do produto[/]", choices=ids_validos)
        
        novo_produto = {"nome": nome, "preco": preco, "categoriaId": cat_id}
        requests.post(f"{API_URL}/produtos", json=novo_produto)
        console.print("[bold #50C878]Produto cadastrado com sucesso![/bold #50C878]")

    elif acao == "2":
        produtos = requests.get(f"{API_URL}/produtos").json()
        
        table = Table(title="Lista de Produtos", title_style="bold #32CD32", border_style="#32CD32")
        table.add_column("ID", style="#00D7FF", justify="center")
        table.add_column("Nome", style="#FFB6C1")
        table.add_column("Preco", style="#50C878")
        table.add_column("ID Categoria", justify="center", style="#8A2BE2")
        
        for p in produtos:
            table.add_row(str(p.get("id")), p.get("nome"), f"R$ {p.get('preco'):.2f}", str(p.get("categoriaId")))
        console.print(table)