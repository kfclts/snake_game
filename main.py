from turtle import Turtle, Screen

screen = Screen()
# screen_width, screen_height = screen.window_width() // 2, screen.window_height() // 2
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")


starting_postion = [(0,0), (-20, 0), (-40, 0)]

for postion in starting_postion:
    segment = Turtle(shape="square")
    segment.color("white")
    segment.goto(postion)

# segment_1 = Turtle(shape="square")
# segment_1.color("white")

# segment_2 = Turtle(shape="square")
# segment_2.color("white")
# segment_2.goto(-20, 0)

# segment_3 = Turtle(shape="square")
# segment_3.color("white")
# segment_3.goto(-40, 0)




screen.exitonclick()