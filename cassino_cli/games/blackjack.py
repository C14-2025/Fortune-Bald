import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from cassino_cli.utils.deck import new_shuffled_deck, hand_value, format_hand

console = Console()

def _deal_card(deck):
    if not deck:
        deck.extend(new_shuffled_deck(4))
    return deck.pop()

def _get_player_action():
    while True:
        escolha = click.prompt("Ação (h = hit, s = stand, d = double) ", default="h").lower()
        if escolha in ['h', 's', 'd']:
            return escolha
        console.print("[red]Opção inválida. Tente novamente.[/red]")

def _dealer_play(dealer, deck):
    while hand_value(dealer) < 17 or (hand_value(dealer) == 17 and any(r == "A" for r, _ in dealer)):
        dealer.append(_deal_card(deck))

def play_blackjack(saldo_inicial: int, aposta: int):
    saldo = saldo_inicial
    deck = new_shuffled_deck(4)

    while saldo >= aposta:
        console.rule("[bold]Blackjack[/bold]")
        console.print(f"Saldo: [bold]${saldo}[/bold] | Aposta base: [bold]${aposta}[/bold]")

        round_bet = aposta
        player = [_deal_card(deck), _deal_card(deck)]
        dealer = [_deal_card(deck), _deal_card(deck)]

        while True:
            table = Table(title="Mesa")
            table.add_column("Jogador", justify="left")
            table.add_column("Dealer", justify="left")
            table.add_row(
                f"{format_hand(player)}  (valor: {hand_value(player)})",
                f"[{dealer[0][0]}{dealer[0][1]}] [??]  (parcial)"
            )
            console.print(table)

            if hand_value(player) == 21:
                console.print(Panel.fit("Blackjack! Você ganhou 1.5x", style="green"))
                ganho = int(round_bet * 1.5)
                saldo += ganho
                break

            escolha = _get_player_action()

            if escolha == "h":
                player.append(_deal_card(deck))
                if hand_value(player) > 21:
                    console.print(Panel.fit("Estourou! Você perdeu.", style="red"))
                    saldo -= round_bet
                    break
                continue

            if escolha == "d":
                if saldo >= round_bet * 2:
                    round_bet *= 2
                    console.print(f"Aposta dobrada para ${round_bet}.")
                    player.append(_deal_card(deck))
                    if hand_value(player) > 21:
                        console.print(Panel.fit("Estourou após dobrar!", style="red"))
                        saldo -= round_bet
                        break
                    _dealer_play(dealer, deck)
                else:
                    console.print(Panel.fit("Saldo insuficiente para dobrar.", style="yellow"))
                    continue

            if escolha == "s":
                _dealer_play(dealer, deck)

            pv, dv = hand_value(player), hand_value(dealer)
            mesa_final = Table(title="Resultado")
            mesa_final.add_column("Jogador")
            mesa_final.add_column("Dealer")
            mesa_final.add_row(
                f"{format_hand(player)}  (valor: {pv})",
                f"{format_hand(dealer)}  (valor: {dv})"
            )
            console.print(mesa_final)

            if dv > 21 or pv > dv:
                console.print(Panel.fit("Você venceu!", style="green"))
                saldo += round_bet
            elif pv < dv:
                console.print(Panel.fit("Dealer venceu.", style="red"))
                saldo -= round_bet
            else:
                console.print(Panel.fit("Empate (push).", style="yellow"))

            break

        if saldo < 1:
            console.print(Panel.fit("Saldo zerado. Fim de jogo.", style="red"))
            break

        again = click.confirm("Jogar outra rodada?", default=True)
        if not again:
            break

    console.print(Panel.fit(f"Saldo final: ${saldo}", style="cyan"))
    return saldo
