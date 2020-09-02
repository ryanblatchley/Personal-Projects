"""
Author: Ryan Blatchley
Description: Simple blackjack game using python
"""

import random

#house's cards

dealer_cards = []

#player's cards

player_cards = []

#dealer cards again
while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1, 11))
    if len(dealer_cards) == 2:
        print("Dealer has: ", dealer_cards)
