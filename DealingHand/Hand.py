"""
Hand.py
Contains the class Hand that can store a requested amount of
Card objects, retrieve their black jack value, and can add more
Card objects
"""

import Card
import random

class Hand:
    """
    One object stores Cards requested by the client, can retrieve
    the total black jack value of the cards, and store another Card object
    """
    def __init__(self, numCardsInHand):
        """
        Stores the requested number of random Card objects
        @param: numCardsInHand Integer of how many cards the
        clients requests to be in the Hand Object
        """
        self.numCardsInHand = numCardsInHand
        self.suitList = ['h', 'c', 's', 'd']
        self.cardsInHandList = []
        for card in range(0, numCardsInHand):
            suit = random.choice(self.suitList)
            rank = random.randint(1, 13)
            object = Card.Card(rank, suit)
            self.cardsInHandList.append(object)

    def bjValue(self):
        """
        Returns the total black jack value of all the Cards in the Hand
        @return: total The sum of all black jack values in a Hand object
        """
        total = 0
        for bjValuecard in self.cardsInHandList:
            bjValue = bjValuecard.bjValue()
            total += bjValue
        return total

    def __str__(self):
        """
        Prints all cards in the Hand Object
        @return: "%s" % hand String of all Cards in the Hand
        """
        hand = ""
        for card in self.cardsInHandList:
            hand += "\n" + card.__str__()
        return "%s" % hand

    def hitMe(self):
        """
        Adds another Card object to the Hand
        """
        newSuit = random.choice(self.suitList)
        newRank = random.randint(1, 13)
        object = Card.Card(newRank, newSuit)
        self.cardsInHandList.append(object)


