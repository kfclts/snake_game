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
    segment.penup()     # without draw, will not have a white line
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

# game_is_on = True
# while game_is_on:
k = 10
while k > 0:
    screen.update()
    time.sleep(0.2)
    # for seg in segments:
    #     seg.forward(20)
    ## revise the order,
    for seg_num in range(len(segments) - 1, 0, -1):  # start = 2, stop = 0, setp = -1 => 2, 1, 0 
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()  
        segments[seg_num].goto(new_x, new_y)  # 3rd pixel move to 2nd pixel, 2nd pixel move to 1st pixel
    segments[0].forward(20)
    k -=1


screen.exitonclick()