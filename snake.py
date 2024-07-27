
from turtle import Turtle
STARTING_POSTION = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        for postion in STARTING_POSTION:
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()     # without draw, will not have a white line
            segment.goto(postion)
            self.segments.append(segment)
            
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # start = 2, stop = 0, setp = -1 => 2, 1, 0 
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()  
            self.segments[seg_num].goto(new_x, new_y)  # 3rd pixel move to 2nd pixel, 2nd pixel move to 1st pixel
        self.segments[0].forward(MOVE_DISTANCE)
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)