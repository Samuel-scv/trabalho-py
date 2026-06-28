import requests
from rich.console import Console

console = Console()
API_URL = "http://localhost:3000"

def pesquisa_avancada():
    console.print("\n[bold #FFAF00]─── Pesquisa Avancada de Produtos ───[/bold #FFAF00]")
    termo = input("Digite parte do nome do produto: ").lower()
    
    try:
        preco_maximo = float(input("Digite o preco maximo (ou 0 para ignorar): "))
    except ValueError:
        console.print("\n[bold #FF005F]Valor invalido para o preco. Retornando ao menu...[/bold #FF005F]")
        return
    
    try:
        produtos = requests.get(f"{API_URL}/produtos").json()
    except requests.exceptions.RequestException:
        console.print("\n[bold #FF005F]Erro ao conectar com o banco de dados. Retornando ao menu...[/bold #FF005F]")
        return

    resultados = []
    
    for p in produtos:
        match_nome = termo in p.get("nome", "").lower()
        match_preco = (preco_maximo == 0) or (float(p.get("preco", 0)) <= preco_maximo)
        
        if match_nome and match_preco:
            resultados.append(p)
            
    if len(resultados) > 0:
        console.print("\n[bold #50C878]Resultados Encontrados:[/bold #50C878]")
        for r in resultados:
            console.print(f"[#FFB6C1]{r['nome']}[/] - [#50C878]R$ {r['preco']}[/]")
            
    if len(resultados) == 0:
        if termo != "":
            console.print(f"\n[bold #FF005F]O produto '{termo}' nao foi achado.[/bold #FF005F]")
        else:
            console.print("\n[bold #FF005F]Nenhum produto foi achado com esses criterios.[/bold #FF005F]")