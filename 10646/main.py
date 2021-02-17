import sys
from collections import defaultdict

inputs = []
if __name__ == "__main__":
    inputs = sys.stdin.read().splitlines()

# with open('input.txt') as f:
#     for line in f:
#         inputs.append(line)

num_cases = int(inputs[0])
i = 1

def default_10():
    return 10

# build value mapping
val_map = defaultdict(default_10)
for val in range(2, 10):
    val_map[str(val)] = val

def get_card_val(card):
    return val_map[card[0]]

def get_cards(Y, deck):
    card = deck[-1]
    X = get_card_val(card)
    Y = X + Y
    index = len(deck) - (11 - X)
    deck = deck[0:index]
    
    return Y, deck

def play_game(deck):
    Y = 0
    removed_pile = deck[25:]
    remaining_pile = deck[:25]
    for _ in range(0, 3):
        Y, remaining_pile = get_cards(Y, remaining_pile)
    final_cards = remaining_pile + removed_pile

    return final_cards[Y-1]


for index in range(i, num_cases+1):
    deck = inputs[index].split(' ')
    print("Case %s: %s" % (index, play_game(deck)))
exit(0)