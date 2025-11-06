import random
import time
import click
from rich.console import Console
from rich.panel import Panel
from rich.align import Align

console = Console()

SYMBOLS = ["🍒", "🍋", "⭐", "🔔", "7️⃣"]

PAYOUTS = {
    ("🍒", "🍒", "🍒"): 5,
    ("🍋", "🍋", "🍋"): 8,
    ("⭐", "⭐", "⭐"): 12,
    ("🔔", "🔔", "🔔"): 20,
    ("7️⃣", "7️⃣", "7️⃣"): 50,
    "pair": 2
}

def _spin():
    return [random.choice(SYMBOLS) for _ in range(3)]

def _payout(combo):
    t = tuple(combo)
    if t in PAYOUTS:
        return PAYOUTS[t]
    if combo[0] == combo[1] or combo[1] == combo[2] or combo[0] == combo[2]:
        return PAYOUTS["pair"]
    return 0

def play_slots(saldo_inicial: int, aposta: int):

    saldo = saldo_inicial
    console.rule("[bold]Caça-Níquel[/bold]")

    try:
        while saldo >= aposta:
            console.print(f"Saldo: [bold]${saldo}[/bold] | Aposta: [bold]${aposta}[/bold]")
            click.confirm("Girar?", default=True, abort=True)

            reels = [" ", " ", " "]
            for i in range(10):
                reels = _spin()
                panel = Panel(Align.center(" | ".join(reels), vertical="middle"), title="Girando…")
                console.clear()
                console.print(panel)
                time.sleep(0.07 + i * 0.01)

            ganho_mult = _payout(reels)
            ganho = aposta * ganho_mult
            saldo = saldo - aposta + ganho

            if ganho_mult > 0:
                console.print(Panel.fit(f"🎉 {reels}  Você ganhou x{ganho_mult} = ${ganho}!", style="green"))
            else:
                console.print(Panel.fit(f"{reels}  Nada desta vez. 😅", style="red"))

            if saldo < aposta:
                console.print(Panel.fit("Saldo insuficiente para continuar.", style="yellow"))
                break

            if not click.confirm("Girar novamente?", default=True):
                break

    except click.Abort:
        console.print(Panel.fit("Operação cancelada. Voltando ao menu…", style="yellow"))

    console.print(Panel.fit(f"Saldo final: ${saldo}", style="cyan"))
    return saldo
