from turtle import Screen
from snake import Snake
from food import Food
from score_board import Scoreboard
import time
import random


screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_forward()

    #detect collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        colors = ["red", "orange","green","black","pink" ]
        bg_color = random.choice(colors)
        screen.bgcolor(bg_color)

    

    #detect collision with wall
    if snake.head.xcor()>285 or snake.head.xcor()<-285 or snake.head.ycor()>285 or snake.head.ycor()<-285:
        scoreboard.reset()
        snake.reset()

    #detect collision with tail
    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment)<10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()

