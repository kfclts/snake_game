from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # defaul is 20, streth to 0.5, is 10
        self.color("blue")
        self.speed("fastest") ## will not see the location created, but show up at the location goto
        random_x = random.randint(-280, 280) # to prevent collipse the wall
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        
        
    