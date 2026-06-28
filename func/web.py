import requests
import os
import webbrowser
from rich.console import Console

console = Console()
API_URL = "http://localhost:3000"

def gerar_pagina_web():
    produtos = requests.get(f"{API_URL}/produtos").json()
    
    html = """
    <html>
    <head><title>Relatório de Produtos</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
    </style>
    </head>
    <body>
        <h2>Relatório da Tabela Principal (Produtos)</h2>
        <table>
            <tr><th>ID</th><th>Nome</th><th>Preço</th><th>Categoria ID</th></tr>
    """
    for p in produtos:
        html += f"<tr><td>{p.get('id')}</td><td>{p.get('nome')}</td><td>R$ {p.get('preco')}</td><td>{p.get('categoriaId')}</td></tr>"
    
    html += """
        </table>
    </body>
    </html>
    """
    
    with open("relatorio.html", "w", encoding="utf-8") as file:
        file.write(html)
    
    console.print("[green]Página web gerada com sucesso! Abrindo no navegador...[/green]")
    webbrowser.open('file://' + os.path.realpath("relatorio.html"))