from collections import Counter


class Cards:
    def __init__(self, hand, bid, strength):
        self.hand = hand
        self.bid = int(bid)
        self.strength = strength
   
from collections import Counter

def check_hand_value(hand):
    # Count the occurrences of each card
    card_counts = Counter(hand)
    extra = 0

    ##this if statement is for part 2 only
    if card_counts["J"] != 0:
        numof_j = card_counts["J"]
        card_counts["J"] = 0 # reset and don't count the J

        max_value = max(card_counts.values())
        for i in range(numof_j):
            max_value += 1
            if max_value == 2:
                extra += 1
            elif max_value == 3:
                extra += 2
            elif max_value == 4:
                extra += 2
            elif max_value == 5:
                extra += 1

    for card, count in card_counts.items():
        if count == 5:
            return 6 

    # Check for four of a kind
    for card, count in card_counts.items():
        if count == 4:
            return 5 + extra

    # Check for full house
    if set(card_counts.values()) == {2, 3}:
        return 4 + extra

    # Check for three of a kind
    for card, count in card_counts.items():
        if count == 3:
            return 3 + extra

    # Check for two pairs
    num_pairs = sum(1 for count in card_counts.values() if count == 2)
    if num_pairs == 2:
        return 2 + extra

    # Check for one pair
    if num_pairs == 1:
        return 1 + extra

    return 0 + extra


def card_value(card):
    if card.isdigit():
        return int(card)
    else:
        ## for part 2 J value is changed to -1
        face_cards = {'A': 14, 'K': 13, 'Q': 12, 'J': -1, 'T': 10}
        return face_cards[card]


def custom_sort_key(x):
    return x.strength, [card_value(card) for card in x.hand]


def part1(lines):
    winnings = 0
    ranked= []
    for line in lines:
        hand,bid = line.split()
        cards = Cards(hand,bid, check_hand_value(hand))
        ranked.append(cards)

    ranked = sorted(ranked, key=custom_sort_key)
   
    for j in range(len(ranked)):
        print(ranked[j].hand,ranked[j].strength,j+1)
   
    for r in range(len(ranked)):       
        winnings+=ranked[r].bid*(r+1)

    print(winnings)
   
if __name__ == "__main__": 
    file_path = "./day7/input.txt"
    with open(file_path, 'r') as file:
        lines = file.readlines()
    part1(lines)
    