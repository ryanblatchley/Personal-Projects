"""
Author: Ryan Blatchley
Description: Simple blackjack game using python
"""

import random

#house's cards

dealer_cards = []

#player's cards

player_cards = []

#card dealing phase

#dealer cards
while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1, 11))
    if len(dealer_cards) == 2:
        print("")
        print("Dealer has: ", dealer_cards[0], " , X", sep=(""))
        print("")

#player cards
while len(player_cards) != 2:
    player_cards.append(random.randint(1, 11))
    if len(player_cards) == 2:
        print("player has has: ", player_cards[0], " , ", player_cards[1], " for a total of: ", player_cards[0] + player_cards[1],  sep=(""))
        print("")
