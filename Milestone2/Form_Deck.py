import random


'''
I want this one to object orient a deck of cards program
each card will have a name a suit and a value
'''

#this one creates the card with its suit, name and value
class Card:
    def __init__(self,suit,name,value):
        self.name = name
        self.suit = suit
        self.value = value
    def __str__(self):
        return f'{self.name} of {self.suit}'

suits = ['Hearts','Diamonds','Spades','Clubs']
values = [('Ace',11),('Two',2),('Three',3),('Four',4),('Five',5),('Six',6),('Seven',7),('Eight',8),('Nine',9),
          ('Ten',10),('Jack',10),('Queen',10),('King',10)]

#this makes the entire deck in the format of the cards class
class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in suits:
            for v in values:
                    self.cards.append(Card(s,v[0],v[1]))

    def show(self):
        for c in self.cards:
            print(c)

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw(self):
        return self.cards.pop()


if __name__ == '__main__':
    deck = Deck()
    deck.build()
    deck.shuffle()  #these three will shuffle the deck
    card = deck.draw()#is all you really need for drawing a car from it

