import requests
import matplotlib.pyplot as plt
from rich.console import Console

console = Console()
API_URL = "http://localhost:3000"

def gerar_grafico():
    console.print("\n[bold magenta]--- Gráfico: Quantidade de Produtos por Categoria ---[/bold magenta]")
    produtos = requests.get(f"{API_URL}/produtos").json()
    categorias = requests.get(f"{API_URL}/categorias").json()
    
    mapa_categorias = {str(c['id']): c['nome'] for c in categorias}
    contagem = {nome: 0 for nome in mapa_categorias.values()}
    
    for p in produtos:
        cat_id = str(p.get("categoriaId"))
        if cat_id in mapa_categorias:
            nome_cat = mapa_categorias[cat_id]
            contagem[nome_cat] += 1
            
    nomes = list(contagem.keys())
    valores = list(contagem.values())
    
    plt.bar(nomes, valores, color=['blue', 'green', 'red', 'purple'])
    plt.title('Número de Produtos por Categoria')
    plt.xlabel('Categorias')
    plt.ylabel('Quantidade de Produtos')
    plt.show()