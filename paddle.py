from turtle import Turtle

class Paddle (Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("orange")
        self.penup()
        self.goto(position)
        self.shapesize(1,5)
    
    def go_left(self):
        new_x = self.xcor()-70
        if new_x > -380:
            self.goto(new_x, self.ycor())
    def go_right(self):
        new_x = self.xcor()+70
        if new_x < 380:
            self.goto(new_x, self.ycor())