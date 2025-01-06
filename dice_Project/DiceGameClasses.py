'''
This file will have the classes to make the DiceGameProgram work

'''
import random

class Die:

    def __init__(self, number_of_Sides):

        self.number_of_Sides = number_of_Sides
        self.face_Up_Value = 1

    def roll(self):

        self.face_Up_Value = random.randint(1, self.number_of_Sides)
       

    def getValue(self):

        return self.face_Up_Value
    
    def __add__(self, other):
        return self.face_Up_Value + other.face_Up_Value
        

    def __gt__(self, other):

        return self.face_Up_Value > other.face_Up_Value
    

class Player:

    def __init__(self, name):
        self.name = name
        self.die1 = Die(6)
        self.die2 = Die(10)

    def rollDice(self):

        self.die1.roll()
        self.die2.roll()
    
    
    def getDiceValue(self):

        return self.die1 + self.die2

    def __str__(self):
        return f'{self.name} rolled {self.getDiceValue()}'



class HighTwoGame:

    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def playOneGame(self):
        self.player1.rollDice()
        self.player2.rollDice()

        if self.player1.getDiceValue() > self.player2.getDiceValue():
            print(f'{self.player1} won!')
            return self.player1

        elif self.player2.getDiceValue() > self.player1.getDiceValue():
            print(f'{self.player2} won!')
            return self.player2
        else:
            print(f'Tie')
            return None
            
        
    

    def playManyGames(self, numberOfGames):
        player1_wins = 0
        player2_wins = 0
    
        for i in range(numberOfGames):
            
            winner = self.playOneGame()
            if winner == self.player1:
                player1_wins += 1
            elif winner == self.player2:
                player2_wins += 1

        if player1_wins > player2_wins:
            print(f'{self.player1} wins!')
        elif player2_wins > player1_wins:
            print(f'{self.player2} wins!')
        else:
            print(f'Tie')        