"""
Caitlin Sheeran
11/8/2024

This program will allow two players to play a dice dame. Each player will
roll a six sided dice and a 10 sided dice. The played with the
higher score will win
"""

from DiceGameClasses import *


print("Game one:")
game1 = HighTwoGame("Matt", "Ashley")
game1.playOneGame()

print("")
print("Game two:")
game2 = HighTwoGame("Dexter", "Eugene")
game2.playOneGame()
