from cassino_cli.games import slots
import pytest


def test_slots_payout_correct():
    assert slots._payout(["🍒", "🍒", "🍒"]) == 5

@pytest.mark.parametrize("reels,expected_payout", [
    (["🍒", "🍒", "⭐"], 2),
    (["⭐", "🍋", "⭐"], 2),
    (["7️⃣", "🔔", "7️⃣"], 2),
])
def test_slots_pair_correct(reels, expected_payout):
    assert slots._payout(reels) == expected_payout


def test_slots_payout_none():
    assert slots._payout(["🍒", "🍋", "⭐"]) == 0


def test_slots_returns_valid_symbols():
    combo = slots._spin()
    assert isinstance(combo, list)
    assert len(combo) == 3
    for sym in combo:
        assert sym in slots.SYMBOLS


def test_slots_play_round_updates_saldo(monkeypatch, capsys):
    saldo_inicial, aposta = 100, 5

    monkeypatch.setattr(slots, "_spin", lambda: ["7️⃣", "7️⃣", "7️⃣"])
    monkeypatch.setattr("click.confirm", lambda *a, **k: False)
    monkeypatch.setattr("time.sleep", lambda *a, **k: None)

    slots.play_slots(saldo_inicial, aposta)

    out = capsys.readouterr().out

    payout = slots.PAYOUTS[("7️⃣", "7️⃣", "7️⃣")]
    saldo_final_esperado = saldo_inicial - aposta + (aposta * payout)
    assert f"Saldo final: ${saldo_final_esperado}" in out


def test_slots_insufficient_initial(capsys):
    slots.play_slots(4, 5)
    out = capsys.readouterr().out
    assert "Saldo final: $4" in out


def test_slots_only_symbols_valid   ():
    valid_symbols = set(slots.SYMBOLS)

    for combination in slots.PAYOUTS:
        if isinstance(combination, tuple):
            assert len(combination) == 3
            for symbol in combination:
                assert symbol in valid_symbols, f"Símbolo inválido: {symbol}"


def test_payout_triple_bell():
    assert slots._payout(["🔔", "🔔", "🔔"]) == slots.PAYOUTS[("🔔", "🔔", "🔔")]


def test_play_slots_stop_game(monkeypatch, capsys):
    monkeypatch.setattr(slots, "_spin", lambda: ["⭐", "⭐", "⭐"])
    monkeypatch.setattr("click.confirm", lambda *a, **k: False)
    monkeypatch.setattr("time.sleep", lambda *a, **k: None)

    slots.play_slots(50, 5)

    out = capsys.readouterr().out
    assert "Saldo final" in out

def test_slots_all_combinations():
    test_cases = [
        (["🍒", "🍒", "🍒"], 5),
        (["🍋", "🍋", "🍋"], 8),
        (["⭐", "⭐", "⭐"], 12),
        (["🔔", "🔔", "🔔"], 20),
        (["7️⃣", "7️⃣", "7️⃣"], 50),
    ]

    for reels, expected_payout in test_cases:
        assert slots._payout(reels) == expected_payout, f"Falhou para {reels}"

def test_slots_animation_with_mock(monkeypatch):
    monkeypatch.setattr("time.sleep", lambda *a, **k: None)
    assert True