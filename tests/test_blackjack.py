from cassino_cli.games import blackjack
import pytest


def test_blackjack_deal_card_refills_deck(monkeypatch):
    monkeypatch.setattr(
        blackjack,
        "new_shuffled_deck",
        lambda n: [("A", "♠"), ("K", "♥")]
    )

    deck = []
    card = blackjack._deal_card(deck)
    assert card == ("K", "♥")
    assert len(deck) == 1
    assert deck[0] == ("A", "♠")

def test_blackjack_no_round_when_saldo_less_than_aposta(capsys):
    blackjack.play_blackjack(saldo_inicial=5, aposta=10)
    out = capsys.readouterr().out
    assert "Saldo final: $5" in out

def test_valor_mao_com_as_e_cartas_altas():
    mao = [("A", "♠"), ("9", "♥")]
    assert blackjack.hand_value(mao) == 20

def test_valor_mao_com_dois_as():
    mao = [("A", "♠"), ("A", "♥")]
    assert blackjack.hand_value(mao) == 12

def test_blackjack_player_busts(monkeypatch, capsys):
    def mock_deal_card(deck):
        if not deck:
            deck.extend([("K", "♣"), ("Q", "♦"), ("9", "♥"), ("8", "♠")])
        return deck.pop()

    def mock_get_player_action():
        return "h"

    monkeypatch.setattr(blackjack, "_deal_card", mock_deal_card)
    monkeypatch.setattr(blackjack, "_get_player_action", mock_get_player_action)
    monkeypatch.setattr("click.confirm", lambda *a, **k: False)

    blackjack.play_blackjack(saldo_inicial=100, aposta=10)

    out = capsys.readouterr().out
    assert "Estourou" in out or "Dealer venceu" in out

def test_format_hand():
    mao = [("A", "♠"), ("K", "♥"), ("10", "♦")]
    formatted = blackjack.format_hand(mao)
    assert formatted == "[A♠] [K♥] [10♦]"