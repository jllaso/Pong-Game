from turtle import Screen
from paddle import Paddle
import time
from ball import Ball
import random
from scoreboard import Scoreboard
#Set up screen and paddle action listeners

FPS = 60
dt = 1.0 / FPS

scores = [5, 8, 11]
max_score = 0
difficulty_level = input("Welcome to PONG!!!\nWhat level of difficulty do you choose? (Easy/Medium/Hard): ")
if difficulty_level.lower() == 'easy':
    max_score = scores[0]
elif difficulty_level.lower() == 'medium':
    max_score = scores[1]
elif difficulty_level.lower() == 'hard':
    max_score = scores[2]
else:
    raise Exception('Sorry, you need to choose a difficulty level')
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)
player2_paddle = Paddle('blue', 1)
player1_paddle = Paddle('orange', 2)
ball = Ball(difficulty_level)
scoreboard = Scoreboard()
ball.launch(random.choice([-1, 1]))
screen.listen()
screen.onkey(player2_paddle.move_paddle_up, 'Up')
screen.onkey(player2_paddle.move_paddle_down, 'Down')
screen.onkey(player1_paddle.move_paddle_up, 'W')
screen.onkey(player1_paddle.move_paddle_down, 'S')


screen.update()

is_game_on = True

while is_game_on:
    ball.move(dt)
    screen.update()
    time.sleep(dt)

    if scoreboard.score_2 == max_score and scoreboard.score_1 < max_score:
        is_game_on = False
        scoreboard.game_over()
    elif scoreboard.score_1 == max_score and scoreboard.score_2 < max_score:
        is_game_on = False
        scoreboard.game_over()
    elif scoreboard.score_1 == max_score and scoreboard.score_2 == max_score:
        max_score += 1
        print('Whoever scores wins!')



    if ball.xcor() > 390:
        ball.out_of_bounds(2)
        scoreboard.point_1()
        scoreboard.update_scoreboard()
        screen.update()
    elif ball.xcor() < -390:
        ball.out_of_bounds(1)
        scoreboard.point_2()
        scoreboard.update_scoreboard()
        screen.update()

    elif ball.ycor() > 290 or ball.ycor() < -290:
        ball.wall_bounce()

    if ball.distance(player2_paddle) < 60 and ball.xcor() > 340:
        ball.paddle_bounce(player2_paddle)

    if ball.distance(player1_paddle) < 60 and ball.xcor() < -340:
        ball.paddle_bounce(player1_paddle)

screen.exitonclick()
