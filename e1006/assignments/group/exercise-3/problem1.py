import random

suits = ['♠', '♣', '♦', '♥'] # Feel free to use these symbols to
                             # represent the different suits.

class Card:

    def __init__(self, suit, rank):
        pass # replace this with an implementation

    def __str__(self):
        return '' # replace with an implementation


class CardCollection:

    def __init__(self):
        self.cards = []

    def add_card(self, card):
        pass # replace this with an implementation

    def draw_card(self):
        return None # replace this, must remove and return a Card
                    # instance from self.cards

    def make_deck(self):
        pass   # replace this, initialize self.cards with a fresh
               # list of the 52 playing cards in random order.

    def value(self):
        return 0 # replace this, must return an int representing
                 # the total value of cards in this collection.


def main():
    deck = CardCollection()
    deck.make_deck() # initialize a fresh deck

    player_hand = CardCollection()

    # complete the main method


if __name__ == "__main__":
    main()
