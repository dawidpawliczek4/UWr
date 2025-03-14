import random
from collections import Counter

def get_figure_card():
    cards = [11,12,13,14]
    suits = [0,1,2,3]

    card = random.choice(cards)
    suit = random.choice(suits)

    return (card, suit)

def get_blot_card():
    cards = [i for i in range(7, 11)]
    suits = [0,1,2,3]

    card = random.choice(cards)
    suit = random.choice(suits)

    return (card, suit)

def get_figure_hand():
    hand = []
    while len(hand) < 5:
        card = get_figure_card()
        if card not in hand:
            hand.append(card)
    return hand

def get_blot_hand():
    hand = []
    while len(hand) < 5:
        card = get_blot_card()
        if card not in hand:
            hand.append(card)
    return hand

def is_straight(values):
    """Sprawdza, czy lista wartości kart tworzy strita."""
    unique_values = sorted(set(values))
    # Jeśli nie mamy 5 unikalnych kart, nie jest to strit
    if len(unique_values) != 5:
        return False
    if max(values) - min(values) == 4:
        return True
    # Może być strit z asa ale nie uwzgledniamy strita z asa     
    ####
    return False

def evaluate_hand(hand):
    """    
    zwraca liczbe gdzie:
    1 - poker
    2 - kareta
    3 - full house
    4 - kolor
    5 - strit
    6 - trojka
    7 - dwie pary
    8 - para
    9 - high card
    """
    values = [card for card, suit in hand]
    suits = [suit for card, suit in hand]
    values = sorted(values)
    freq = Counter(values)
    freq_values = list(freq.values())

    flush = (len(set(suits)) == 1)
    straight = is_straight(values)

    if flush and straight:
        return 1
    if 4 in freq_values:
        return 2
    if sorted(freq_values) == [2,3]:
        return 3
    if flush:
        return 4
    if straight:
        return 5
    if 3 in freq_values:
        return 6
    if freq_values.count(2) == 2:
        return 7
    if 2 in freq_values:
        return 8
    return 9



def compare_hands(hand1, hand2):
    hand1_val = evaluate_hand(hand1)
    hand2_val = evaluate_hand(hand2)
    # smaller in eval is better    
    if hand1_val < hand2_val:
        return 'hand1'
    if hand2_val < hand1_val:
        return 'hand2'
    
    hand1_values = sorted([int(card) for card, suit in hand1], reverse=True)
    hand2_values = sorted([int(card) for card, suit in hand2], reverse=True)

    for v1, v2 in zip(hand1_values, hand2_values):
        if v1 > v2:
            return 'hand1'
        if v2 > v1:
            return 'hand2'
        
    return 'tie'
    
def simulate():
    wins = 0
    ties = 0
    for _ in range(100000):        
        blotkarz = get_blot_hand()
        figurant = get_figure_hand()
        res = compare_hands(blotkarz, figurant)        
        if res == 'hand1':
            wins += 1
        elif res == 'tie':
            ties += 1
    return wins / 100000

print(simulate())