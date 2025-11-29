from cassino_cli.games import blackjack
from unittest.mock import patch

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
        mock_print.assert_any_call("Saldo final: $5")

def test_valor_mao_com_as_e_cartas_altas():
    mao = [("A", "♠"), ("9", "♥")]
    assert blackjack._valor_mao(mao) == 20


def test_valor_mao_com_dois_as():
    mao = [("A", "♠"), ("A", "♥")]
    assert blackjack._valor_mao(mao) == 12

def test_dealer_vence_quando_jogador_estoura(monkeypatch):
    with patch("blackjack._valor_mao") as mock_valor, \
         patch("builtins.print") as mock_print:
        mock_valor.side_effect = [25, 18]  # jogador > 21
        blackjack._determine_winner([("K", "♣")], [("Q", "♦")])
        mock_print.assert_any_call("Você estourou! Dealer vence.")

def test_empate_entre_jogador_e_dealer(monkeypatch):
    with patch("blackjack._valor_mao", side_effect=[20, 20]), \
         patch("builtins.print") as mock_print:
        blackjack._determine_winner([("10", "♣")], [("K", "♦")])
        mock_print.assert_any_call("Empate!")

def test_blackjack_ganha_imediato(monkeypatch):
    with patch("blackjack._valor_mao", side_effect=[21, 18]), \
         patch("builtins.print") as mock_print:
        blackjack._determine_winner([("A", "♠"), ("K", "♥")], [("10", "♦")])
        mock_print.assert_any_call("Blackjack! Você venceu!")
