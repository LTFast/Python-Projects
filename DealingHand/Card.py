# Contains a program that tests the Card class, which
# will return the rank, suit, blackjack value, and string that names the card.
# If the rank or the suit is not entered correctly, the program will catch the
# error.

class Card:
    """
    One object of this class returns one card's suit, rank, blackjack value, and
    phrase (in a string form) that describes the card. If a rank or suit is entered
    in correctly, the class will catch the error.
    """
    def __init__(self, rank, suit):
        """
        Sets both rank and suit to the values inputted by the user
        @param: rank An integer that represents the rank of the card
        @param: suit The suit of the card
        """
        if rank < 1 or rank > 13:
            raise ValueError('Rank must be between 1 to 13.')
        if suit not in ['h', 's', 'd', 'c']:
            raise ValueError
        if type(rank) != int:
            raise TypeError()
        if type(suit) != str:
            raise TypeError()
        self._rank = rank
        self._suit = suit

    def getRank(self):
        """
        Returns the rank of the card
        @return: self._rank The rank of the card
        """
        return self._rank
    def getSuit(self):
        """
        Returns the suit of the card
        @return: self._suit The rank of the card
        """
        return self._suit
    def bjValue(self):
        """
        Returns the blackjack value of the card
        @return: bjValue The blackjack of the card
        """
        bjValueList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        bjValue = bjValueList[self._rank - 1]
        return bjValue

    def __str__(self):
        """
        Returns a string phrase that names the card
        @return: cardPhrase The string that returns the name of the card
        """
        rank = {1: 'Ace', 2: 'Two', 3: 'Three', 4:'Four', 5: 'Five', 6: 'Six', 7: 'Seven',
                8: 'Eight', 9: 'Nine', 10: 'Ten',11: 'Jack', 12: 'Queen', 13: 'King'}
        suitDict = {'d': 'Diamonds', 'c': 'Clubs', 'h': 'Hearts', 's': 'Spades'}
        suit = self._suit
        cardPhrase = "%s of %s" % (rank[self._rank], suitDict[suit])
        return cardPhrase
