import sys
from datetime import datetime
import click
from rich.console import Console
from rich.panel import Panel

from cassino_cli.games.blackjack import play_blackjack
from cassino_cli.games.slots import play_slots

console = Console()

def coletar_dados_usuario(idade_minima: int = 18):
    ano_atual = datetime.now().year
    while True:
        try:
            nome = input("Digite seu nome: ").strip()
            if not (nome and nome.replace(" ", "").isalpha()):
                print("Nome inválido. Use apenas letras e não deixe vazio.")
                continue

            ano_str = input(f"Digite seu ano de nascimento (ex: {ano_atual-20}): ").strip()
            if not ano_str.isdigit():
                print("Ano inválido. Digite apenas números.")
                continue

            ano_nasc = int(ano_str)
            if not (1950 <= ano_nasc <= ano_atual):
                print(f"Ano fora do intervalo permitido (1950-{ano_atual}).")
                continue

            idade = ano_atual - ano_nasc
            if idade < idade_minima:
                print(f"É necessário ter pelo menos {idade_minima} anos para jogar!.")
                continue

            return nome, ano_nasc

        except (KeyboardInterrupt, EOFError):
            raise click.Abort()

def app():
    console.print(Panel.fit("🎰 [bold]Fortune-Bald[/bold] – Divirta-se com responsabilidade!"))
    print("--- Bem-vindo ao Fortune-Bald! ---")

    try:
        coletar_dados_usuario()
    except click.Abort:
        console.print("\nOperação cancelada. Até mais! 👋")
        sys.exit(0)

    saldo = 0

    while True:
        print("\nEscolha um jogo:")
        print("1) Blackjack (21)")
        print("2) Caça-Níquel")
        print("0) Sair")
        escolha = input("Opção: ").strip()

        if escolha not in {"0", "1", "2"}:
            print("Opção inválida. Tente novamente.")
            continue

        if escolha == "0":
            console.print(f"\nSaldo final: ${saldo}", style="cyan")
            console.print("Até mais! 👋")
            sys.exit(0)

        if saldo == 0:
            try:
                saldo = click.prompt("Digite seu saldo inicial", type=int)
            except click.Abort:
                console.print("\nOperação cancelada. Até mais! 👋")
                sys.exit(0)

        if escolha == "1":
            try:
                aposta = click.prompt("Digite sua aposta por rodada", type=int)
            except click.Abort:
                console.print("\nOperação cancelada. Voltando ao menu…")
                continue
            novo_saldo = play_blackjack(saldo, aposta)
            if novo_saldo is not None:
                saldo = novo_saldo

        elif escolha == "2":
            try:
                aposta = click.prompt("Digite sua aposta por rodada", type=int)
            except click.Abort:
                console.print("\nOperação cancelada. Voltando ao menu…")
                continue
            novo_saldo = play_slots(saldo, aposta)
            if novo_saldo is not None:
                saldo = novo_saldo

if __name__ == "__main__":
    try:
        app()
    except KeyboardInterrupt:
        console.print("\nAté mais! 👋")
        sys.exit(0)
