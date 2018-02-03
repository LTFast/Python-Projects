"""
Test.py
Tests that the Hand class and all its methods are working properly
and stores one Hand object as a Pickle file and reads it back into
a new Hand object.
"""

from Hand import Hand
import pickle

if __name__ == "__main__":
    # Testing all methods in Hand Class
    hand1 = Hand(2)
    print("Original Set of Cards in Hand:%s" % hand1)
    print("Beginning Black Jack Value: %s" % hand1.bjValue())
    hand1.hitMe()
    print("\nSet of Cards After Calling Hit Me: %s" % hand1)
    print("Black Jack Value After 'Hit Me': \n%s" % hand1.bjValue())

    # Extra Credit
    with open('data.pickle', 'wb') as f:
        pickle.dump(hand1, f, pickle.HIGHEST_PROTOCOL)
        f.close()
    with open('data.pickle', 'rb') as g:
        hand2 = pickle.load(g)
        print("\nNew Hand Object from Pickle File: %s" % hand2)

# Output Is:
"""
Original Set of Cards in Hand:
Four of Clubs
Three of Hearts
Beginning Black Jack Value: 7

Set of Cards After Calling Hit Me:
Four of Clubs
Three of Hearts
Five of Clubs
Black Jack Value After 'Hit Me':
12

New Hand Object from Pickle File:
Four of Clubs
Three of Hearts
Five of Clubs
"""







