import requests
import csv
from rich.console import Console

console = Console()
API_URL = "http://localhost:3000"

def gerar_backup():
    console.print("\n[bold #00D7FF]─── Gerar Backup CSV ───[/bold #00D7FF]")
    produtos = requests.get(f"{API_URL}/produtos").json()
    
    if not produtos:
        console.print("[bold #FF005F]Nao ha dados para fazer backup.[/bold #FF005F]")
        return
        
    chaves = produtos[0].keys()
    
    with open('backup_produtos.csv', 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=chaves)
        dict_writer.writeheader()
        dict_writer.writerows(produtos)
        
    console.print("[bold #50C878]Backup realizado com sucesso no arquivo 'backup_produtos.csv'![/bold #50C878]")