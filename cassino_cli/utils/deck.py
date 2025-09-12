import random
from typing import List, Tuple

Card = Tuple[str, str]  # (rank, suit)

RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
SUITS = ["♠", "♥", "♦", "♣"]

def new_shuffled_deck(n_decks: int = 1) -> List[Card]:
    deck = [(r, s) for r in RANKS for s in SUITS] * n_decks
    random.shuffle(deck)
    return deck

def hand_value(hand: List[Card]) -> int:
    value = 0
    aces = 0
    for (rank, _) in hand:
        if rank in ["J", "Q", "K"]:
            value += 10
        elif rank == "A":
            value += 11
            aces += 1
        else:
            value += int(rank)

    while value > 21 and aces > 0:
        value -= 10
        aces -= 1
    return value

def format_hand(hand: List[Card]) -> str:
    return " ".join([f"[{r}{s}]" for r, s in hand])
