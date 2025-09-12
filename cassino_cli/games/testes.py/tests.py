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
