import requests
import os
import webbrowser
from rich.console import Console

console = Console()
API_URL = "http://localhost:3000"

def gerar_pagina_web():
    console.print("\n[bold #00D7FF]─── Gerando Pagina Web ───[/bold #00D7FF]")
    produtos = requests.get(f"{API_URL}/produtos").json()
    
    html = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Relatorio de Produtos</title>
        <style>
            body { 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                background-color: #f4f7f6; 
                color: #333; 
                margin: 0; 
                padding: 40px; 
                display: flex;
                flex-direction: column;
                align-items: center;
            }
            .container {
                width: 80%;
                max-width: 1000px;
                background: #ffffff;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }
            h2 { 
                text-align: center; 
                color: #4B0082; 
                margin-bottom: 20px;
            }
            table { 
                border-collapse: collapse; 
                width: 100%; 
                border-radius: 8px;
                overflow: hidden;
            }
            th, td { 
                padding: 12px 15px; 
                text-align: left; 
                border-bottom: 1px solid #ddd;
            }
            th { 
                background-color: #4B0082; 
                color: #ffffff; 
                text-transform: uppercase;
                font-size: 14px;
            }
            tr:hover { background-color: #f1f1f1; }
            .price { color: #28a745; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Relatorio de Produtos Cadastrados</h2>
            <table>
                <tr><th>ID</th><th>Nome</th><th>Preco</th><th>Categoria ID</th></tr>
    """
    for p in produtos:
        html += f"<tr><td>{p.get('id')}</td><td>{p.get('nome')}</td><td class='price'>R$ {p.get('preco'):.2f}</td><td>{p.get('categoriaId')}</td></tr>"
    
    html += """
            </table>
        </div>
    </body>
    </html>
    """
    
    with open("relatorio.html", "w", encoding="utf-8") as file:
        file.write(html)
    
    console.print("[bold #50C878]Pagina web gerada com sucesso! Abrindo no navegador...[/bold #50C878]")
    webbrowser.open('file://' + os.path.realpath("relatorio.html"))