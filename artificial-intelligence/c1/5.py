import itertools
from collections import Counter

def is_straight(values):
    unique_values = sorted(set(values))
    if len(unique_values) != 5:
        return False
    if unique_values[-1] - unique_values[0] == 4:
        return True
    return False

def evaluate_hand(hand):
    """    
    9 - poker
    8 -kareta itd    
    """
    # Wyciągamy tylko wartości kart (ignorujemy kolory przy ocenie, poza flush)
    values = sorted([card for card, suit in hand])
    suits = [suit for card, suit in hand]
    freq = Counter(values)
    freq_values = list(freq.values())
    flush = (len(set(suits)) == 1)
    straight = is_straight(values)
    
    if flush and straight:
        return 9
    if 4 in freq_values:
        return 8
    if sorted(freq_values) == [2, 3]:
        return 7
    if flush:
        return 6
    if straight:
        return 5
    if 3 in freq_values:
        return 4
    if freq_values.count(2) == 2:
        return 3
    if 2 in freq_values:
        return 2
    return 1

def hand_score(hand):
    score = evaluate_hand(hand)
    tie_breaker = tuple(sorted([card for card, suit in hand], reverse=True))
    return (score, tie_breaker)

def build_score_counts(deck):
    score_counts = {}
    for hand in itertools.combinations(deck, 5):
        score = hand_score(hand)
        score_counts[score] = score_counts.get(score, 0) + 1
    return score_counts

def main():
    blot_deck = [(r, s) for r in range(2, 11) for s in [0, 1, 2, 3]]    
    figure_deck = [(r, s) for r in [11, 12, 13, 14] for s in [0, 1, 2, 3]]
        
    blot_scores = build_score_counts(blot_deck)
    fig_scores = build_score_counts(figure_deck)
    
    blot_wins = 0
    fig_wins = 0
    ties = 0
    
    for b_score, b_count in blot_scores.items():
        for f_score, f_count in fig_scores.items():
            if b_score > f_score:
                blot_wins += b_count * f_count
            elif b_score < f_score:
                fig_wins += b_count * f_count
            else:
                ties += b_count * f_count

    total = sum(blot_scores.values()) * sum(fig_scores.values())
    print("Łączna liczba par rąk:", total)
    print("Blotkarz wygrywa: {:.4f}%".format(blot_wins / total * 100))
    print("Figurnaz wygrywa: {:.4f}%".format(fig_wins / total * 100))
    print("Remisy:           {:.4f}%".format(ties / total * 100))

if __name__ == "__main__":
    main()
