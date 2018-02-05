

import random
"""
Model.py
Uses the random function to simulate dice to be rolled at random.
"""

class callRandom:

    def __init__(self):
        self.diceNum1 = 1
        self.diceNum2 = 0

    def randomNum1(self):
        self.diceNum1 = random.randint(1,6)
        return self.diceNum1

    def randomNum2(self):
        self.diceNum2 = random.randint(1,6)
        return self.diceNum2

diceCombo = callRandom()
dice1 = diceCombo.randomNum1()
dice2 = diceCombo.randomNum2()
print(dice1)
print(dice2)



