import builtins
import types
import pytest

from cassino_cli.games import blackjack
from cassino_cli.games import slots
def test_slots_payout_triple_cherries():
    assert slots._payout(["🍒", "🍒", "🍒"]) == 5


def test_slots_payout_pair():
    assert slots._payout(["🍒", "🍒", "⭐"]) == slots.PAYOUTS["pair"] == 2
    assert slots._payout(["⭐", "🍋", "⭐"]) == 2
    assert slots._payout(["⿧", "🔔", "⿧"]) == 2

def test_slots_payout_none():
    assert slots._payout(["🍒", "🍋", "⭐"]) == 0


def test_slots_spin_returns_valid_symbols():
    combo = slots._spin()
    assert isinstance(combo, list) and len(combo) == 3
    for sym in combo:
        assert sym in slots.SYMBOLS
<<<<<<< HEAD

def test_slots_play_one_winning_round_updates_saldo(monkeypatch, capsys):
    # Força o último giro a ser 7-7-7
    monkeypatch.setattr(slots, "_spin", lambda: ["⿧", "⿧", "⿧"])
    # Evita dormir nas animações
    import time
    monkeypatch.setattr(time, "sleep", lambda *_args, **_kw: None)

    # Primeiro confirm = True (girar), segundo = False (não girar de novo)
    confirms = iter([True, False])
    def fake_confirm(*_a, **_kw):
        return next(confirms)
    import click
    monkeypatch.setattr(click, "confirm", fake_confirm)

    saldo_inicial, aposta = 100, 5
    slots.play_slots(saldo_inicial, aposta)
    out = capsys.readouterr().out
    # Ganhou x50: saldo final = 100 - 5 + 250 = 345
    assert "Saldo final: $345" in out


def test_slots_stops_when_insufficient_initial(monkeypatch, capsys):
    # Não entra no loop porque saldo < aposta
    slots.play_slots(4, 5)
    out = capsys.readouterr().out
    assert "Saldo final: $4" in out

def test_slots_payouts_map_uses_only_known_symbols():
    valid = set(slots.SYMBOLS)
    for k in slots.PAYOUTS:
        if isinstance(k, tuple):
            assert len(k) == 3
            for sym in k:
                assert sym in valid

def test_blackjack_deal_card_refills_deck(monkeypatch):
    # new_shuffled_deck retorna 1 carta conhecida
    def fake_new_shuffled_deck(_n):
        return [("A", "♠")]
    monkeypatch.setattr(blackjack, "new_shuffled_deck", fake_new_shuffled_deck)

    deck = []  # vazio -> deve reabastecer
    card = blackjack._deal_card(deck)
    assert card == ("A", "♠")
    # após pop, deck fica vazio de novo
    assert deck == []


def test_blackjack_no_round_when_saldo_less_than_aposta(capsys):
    # Não entra no while; apenas imprime saldo final
    blackjack.play_blackjack(saldo_inicial=5, aposta=10)
    out = capsys.readouterr().out
    assert "Saldo final: $5" in out
=======
# tests/test_blackjack_flow.py
import builtins
import blackjack_game  

def test_hit_bust_no_dealer_play_and_balance_drop(monkeypatch, capsys):
    fixed_deck = [
        ("2", "C"), ("3", "D"),
        ("5", "H"),
        ("Q", "S"),
        ("7", "D"),
        ("K", "C"),
        ("Q", "H"),
    ]

    monkeypatch.setattr(blackjack_game, "new_shuffled_deck", lambda n: fixed_deck.copy())
    monkeypatch.setattr(blackjack_game, "_get_player_action", lambda: "h")

    import click
    monkeypatch.setattr(click, "confirm", lambda *args, **kwargs: False)

    blackjack_game.play_blackjack(saldo_inicial=100, aposta_inicial=10)

    out, _ = capsys.readouterr()

    assert "Estourou" in out
    assert "Resultado" not in out
    assert "Saldo final: $90" in out.replace("\u00a0", " ")
>>>>>>> 0377789 (Teste Blackjack)
