import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"    


class Deck:
    def __init__(self):
        self.cards = []
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        for rank in ranks:
            for suit in suits:
                self.cards.append(Card(rank, suit))
        random.shuffle(self.cards)


    def deal_cards(self, player1, player2):
        while len(self.cards) > 0:
            card = self.cards.pop()
            player1.add_cards(card)
            if len(self.cards) > 0:
                card = self.cards.pop()
                player2.add_cards(card)


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def add_cards(self, card):
        self.hand.append(card)

    def display_cards(self):
        for card in self.hand:
            print(card)

player1 = Player("1")
player2 = Player("2")

deck = Deck()
deck.deal_cards(player1, player2)

print(f"Player 1 has {len(player1.hand)} cards.")
player1.display_cards()
player2.display_cards()


