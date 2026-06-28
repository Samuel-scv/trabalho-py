from rich.console import Console
from rich.prompt import Prompt

# Importando as funções dos seus respectivos arquivos isolados
from func.categorias import gerenciar_categorias
from func.produtos import gerenciar_produtos
from func.pesquisa import pesquisa_avancada
from func.grafico import gerar_grafico
from func.web import gerar_pagina_web
from func.backup import gerar_backup

console = Console()

def menu():
    while True:
        console.print("\n[bold white on black] --- MENU DO SISTEMA --- [/bold white on black]")
        console.print("1. Gerenciar Categorias (Tabela Auxiliar)")
        console.print("2. Gerenciar Produtos (Tabela Principal)")
        console.print("3. Pesquisa Avançada")
        console.print("4. Gráfico Comparativo")
        console.print("5. Gerar Página Web")
        console.print("6. Gerar Backup (CSV)")
        console.print("0. Sair")
        
        opcao = Prompt.ask("Escolha uma opção", choices=["0", "1", "2", "3", "4", "5", "6"])
        
        if opcao == "1": gerenciar_categorias()
        elif opcao == "2": gerenciar_produtos()
        elif opcao == "3": pesquisa_avancada()
        elif opcao == "4": gerar_grafico()
        elif opcao == "5": gerar_pagina_web()
        elif opcao == "6": gerar_backup()
        elif opcao == "0":
            console.print("[bold red]Saindo do sistema...[/bold red]")
            break

if __name__ == "__main__":
    menu()