import requests
import plotly.express as px
from rich.console import Console

console = Console()
API_URL = "http://localhost:3000"

def gerar_grafico():
    console.print("\n[bold #FF69B4]─── Gerando Grafico Interativo ───[/bold #FF69B4]")
    
    try:
        produtos = requests.get(f"{API_URL}/produtos").json()
        categorias = requests.get(f"{API_URL}/categorias").json()
    except requests.exceptions.RequestException:
        console.print("\n[bold #FF005F]Erro de Conexao: O servidor esta desligado. Retornando ao menu...[/bold #FF005F]")
        return
    
    if not produtos:
        console.print("[bold #FF005F]Nao ha produtos cadastrados para gerar o grafico.[/bold #FF005F]")
        return
        
    mapa_categorias = {str(c['id']): c['nome'] for c in categorias}
    contagem = {nome: 0 for nome in mapa_categorias.values()}
    
    for p in produtos:
        cat_id = str(p.get("categoriaId"))
        if cat_id in mapa_categorias:
            nome_cat = mapa_categorias[cat_id]
            contagem[nome_cat] += 1
            
    fig = px.bar(
        x=list(contagem.keys()),
        y=list(contagem.values()),
        title="Quantidade de Produtos por Categoria",
        labels={'x': 'Categorias', 'y': 'Numero de Produtos'}, 
        color=list(contagem.keys())
    )
    
    fig.update_layout(showlegend=False)
    
    console.print("[bold #50C878]Grafico gerado! Abrindo no seu navegador...[/bold #50C878]")
    fig.show()