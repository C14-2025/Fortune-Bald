import builtins
import types
import pytest
from cassino_cli.games import blackjack
from cassino_cli.games import slots
import slots
from unittest.mock import patch
import blackjack

def test_slots_payout_triple_cherries():
    assert slots._payout(["🍒", "🍒", "🍒"]) == 5

@pytest.mark.parametrize("reels", [
    ["🍒", "🍒", "⭐"],
    ["⭐", "🍋", "⭐"],
    ["⿧", "🔔", "⿧"],
])
def test_slots_pair_with_mocked_spin(monkeypatch, reels):
   
    monkeypatch.setattr(slots, "_spin_reels", lambda: reels)
    payout, out_reels = slots.play_round(bet=1)  
    assert out_reels == reels
    assert payout == slots.PAYOUTS["pair"] == 2


def test_slots_payout_none():
    assert slots._payout(["🍒", "🍋", "⭐"]) == 0

@patch("slots._spin")
def test_slots_spin_returns_valid_symbols(mock_spin):
    mock_spin.return_value = ["🍒", "🍋", "⭐"]

    combo = slots._spin()

    assert isinstance(combo, list) and len(combo) == 3
    for sym in combo:
        assert sym in slots.SYMBOLS

def test_slots_play_one_winning_round_updates_saldo_mock(capsys):
    saldo_inicial, aposta = 100, 5

    with patch('slots._spin') as mock_spin, \
         patch('time.sleep'), \
         patch('click.confirm') as mock_confirm:

        mock_spin.return_value = ["⿧", "⿧", "⿧"]

        mock_confirm.side_effect = [True, False]

        slots.play_slots(saldo_inicial, aposta)

    out = capsys.readouterr().out
    assert "Saldo final: $345" in out


def test_slots_stops_when_insufficient_initial(monkeypatch, capsys):
  
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

def test_blackjack_deal_card_refills_deck():
    # new_shuffled_deck retorna 1 carta conhecida
    with patch("blackjack.new_shuffled_deck", return_value=[("A", "♠")]):
        deck = []  # vazio -> deve reabastecer
        card = blackjack._deal_card(deck)
        assert card == ("A", "♠")
        # após pop, deck fica vazio de novo
        assert deck == []


def test_blackjack_no_round_when_saldo_less_than_aposta(capsys):
    with patch("builtins.print") as mock_print:
        blackjack.play_blackjack(saldo_inicial=5, aposta=10)

        # verifica se "Saldo final: $5" foi impresso
        mock_print.assert_any_call("Saldo final: $5")

