from turtle import Turtle, Screen
import time

screen = Screen()
# screen_width, screen_height = screen.window_width() // 2, screen.window_height() // 2
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # stop update screen


segments = []

starting_postion = [(0,0), (-20, 0), (-40, 0)]

for postion in starting_postion:
    segment = Turtle(shape="square")
    segment.color("white")
    segment.goto(postion)
    segments.append(segment)


screen.update() # update the screen

# segment_1 = Turtle(shape="square")
# segment_1.color("white")

# segment_2 = Turtle(shape="square")
# segment_2.color("white")
# segment_2.goto(-20, 0)

# segment_3 = Turtle(shape="square")
# segment_3.color("white")
# segment_3.goto(-40, 0)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    for seg in segments:
        seg.forward(20)




screen.exitonclick()