from rich.console import Console
from rich.prompt import Prompt
from func.categorias import gerenciar_categorias
from func.produtos import gerenciar_produtos
from func.pesquisa import pesquisa_avancada
from func.grafico import gerar_grafico
from func.web import gerar_pagina_web
from func.backup import gerar_backup

console = Console()

def menu():
    while True:
        console.print("\n[bold #FFFFFF on #4B0082] MENU DO SISTEMA [/bold #FFFFFF on #4B0082]")
        console.print("[#00D7FF]1.[/] Gerenciar Categorias")
        console.print("[#00D7FF]2.[/] Gerenciar Produtos")
        console.print("[#00D7FF]3.[/] Pesquisa Avancada")
        console.print("[#00D7FF]4.[/] Grafico Comparativo")
        console.print("[#00D7FF]5.[/] Gerar Pagina Web")
        console.print("[#00D7FF]6.[/] Gerar Backup (CSV)")
        console.print("[#FF005F]0.[/] Sair")
        
        opcao = Prompt.ask("\n[bold #FFAF00]Escolha uma opcao[/]")
        
        if opcao == "1": gerenciar_categorias()
        elif opcao == "2": gerenciar_produtos()
        elif opcao == "3": pesquisa_avancada()
        elif opcao == "4": gerar_grafico()
        elif opcao == "5": gerar_pagina_web()
        elif opcao == "6": gerar_backup()
        elif opcao == "0":
            console.print("[bold #FF005F]Encerrando o sistema.[/bold #FF005F]")
            break

if __name__ == "__main__":
    menu()