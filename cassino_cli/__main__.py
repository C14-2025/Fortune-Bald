import sys
import click
from rich.console import Console
from rich.panel import Panel

from cassino_cli.games.blackjack import play_blackjack
from cassino_cli.games.slots import play_slots

console = Console()

@click.group(help="Cassino de terminal: Blackjack (21) e Caça-Níquel.")
def app():
    console.print(Panel.fit("🎰 [bold]Cassino CLI[/bold] – Divirta-se com responsabilidade!"))

@app.command(help="Jogar Blackjack (21).")
@click.option("--aposta", default=10, show_default=True, type=int, help="Aposta por rodada.")
def blackjack(aposta: int):
    saldo_inicial = click.prompt("Digite seu saldo inicial", type=int)
    play_blackjack( aposta)

@app.command(help="Jogar Caça-Níquel (3 imagens).")
@click.option("--aposta", default=5, show_default=True, type=int, help="Aposta por rodada.")
def slots(aposta: int):
    saldo_inicial = click.prompt("Digite seu saldo inicial", type=int)
    play_slots(saldo_inicial, aposta)

def coletar_dados_usuario():

    while True:
        nome = input("Digite seu nome: ")
        if nome.strip() and nome.replace(" ", "").isalpha():
            break
        else:
            print("Erro: Nome inválido. Por favor, use apenas letras e não deixe o campo vazio.")

    while True:
        ano_str = input("Digite seu ano de nascimento (ex: 1995): ")
        if ano_str.isdigit():
            ano_nasc = int(ano_str)
            if 1920 <= ano_nasc <= 2023:
                break
            else:
                print("Erro: Ano fora do intervalo permitido (1920-2023).")
        else:
            print("Erro: Ano inválido. Por favor, digite apenas números.")

    return nome.strip(), ano_nasc

print("--- Bem-vindo ao Fortune-Bald! ---")
nome_usuario, ano_usuario = coletar_dados_usuario()

if __name__ == "__main__":
    try:
        app(prog_name="cassino")
    except KeyboardInterrupt:
        console.print("\nAté mais! 👋")
        sys.exit(0)