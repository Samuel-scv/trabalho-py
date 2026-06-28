import requests
from rich.console import Console

console = Console()
API_URL = "http://localhost:3000"

def pesquisa_avancada():
    console.print("\n[bold yellow]--- Pesquisa Avançada de Produtos ---[/bold yellow]")
    termo = input("Digite parte do nome do produto: ").lower()
    preco_maximo = float(input("Digite o preço máximo (ou 0 para ignorar): "))
    
    produtos = requests.get(f"{API_URL}/produtos").json()
    resultados = []
    
    for p in produtos:
        match_nome = termo in p.get("nome", "").lower()
        match_preco = (preco_maximo == 0) or (float(p.get("preco", 0)) <= preco_maximo)
        
        if match_nome and match_preco:
            resultados.append(p)
            
    if resultados:
        for r in resultados:
            console.print(f"Encontrado: {r['nome']} - R$ {r['preco']}")
    else:
        console.print("[red]Nenhum produto encontrado com esses critérios.[/red]")