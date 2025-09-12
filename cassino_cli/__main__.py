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
@click.option("--saldo", default=100, show_default=True, type=int, help="Saldo inicial.")
@click.option("--aposta", default=10, show_default=True, type=int, help="Aposta por rodada.")
def blackjack(saldo: int, aposta: int):
    play_blackjack(saldo, aposta)

@app.command(help="Jogar Caça-Níquel (3 imagens).")
@click.option("--saldo", default=100, show_default=True, type=int, help="Saldo inicial.")
@click.option("--aposta", default=5, show_default=True, type=int, help="Aposta por rodada.")
def slots(saldo: int, aposta: int):
    play_slots(saldo, aposta)

if __name__ == "__main__":
    try:
        app(prog_name="cassino")
    except KeyboardInterrupt:
        console.print("\nAté mais! 👋")
        sys.exit(0)
