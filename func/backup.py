import requests
import csv
from rich.console import Console

console = Console()
API_URL = "http://localhost:3000"

def gerar_backup():
    produtos = requests.get(f"{API_URL}/produtos").json()
    if not produtos:
        console.print("[red]Não há dados para fazer backup.[/red]")
        return
        
    chaves = produtos[0].keys()
    
    with open('backup_produtos.csv', 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=chaves)
        dict_writer.writeheader()
        dict_writer.writerows(produtos)
        
    console.print("[green]Backup realizado com sucesso no arquivo 'backup_produtos.csv'![/green]")