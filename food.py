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
        self.refresh()
        
    def refresh(self):
        min_val, max_val = -280, 280
        step = 20

        min_index = min_val // step
        max_index = max_val // step
        
        random_x = random.randint(min_index, max_index) * step
        random_y = random.randint(min_index, max_index) * step
        self.goto(random_x, random_y)
        
        
    