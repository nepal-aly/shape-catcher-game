from turtle import Turtle
import random
class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.score=0
        self.update_score()
    def update_score(self):
        self.clear()
        self.goto(0,250)
        self.write(f'Score: {self.score}',align='center',font=("courier",26,"normal"))
    
    def increase_score(self,points):
        self.score += points
        self.update_score()
    def reset_score(self):
        self.score =0
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over:" ,align='center',font=("courier",26,"normal"))
    