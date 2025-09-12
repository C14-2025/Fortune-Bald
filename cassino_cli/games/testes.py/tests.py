import builtins
import types
import pytest

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
