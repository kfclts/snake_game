from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
# screen_width, screen_height = screen.window_width() // 2, screen.window_height() // 2
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # stop update screen

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

screen.exitonclick()