from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle_1 = Paddle(350, 0)
paddle_2 = Paddle(-350, 0)

screen.listen()

screen.onkey(paddle_1.go_up, "Up")
screen.onkey(paddle_1.go_down, "Down")

screen.onkey(paddle_2.go_up, "w")
screen.onkey(paddle_2.go_down, "s")

ball = Ball(0, 0)
scoreboard = ScoreBoard()

print(screen.window_width())

move = True

while move:
    time.sleep(ball.move_speed)
    ball.move()

    # To detect the collision with the wal
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()


    # Detecting collisions with the right and left paddle
    if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.move_speed *= 0.9


    # Detect right paddle miss
    if ball.xcor() > 400:
        ball.reset()
        scoreboard.point_l()


    # Detect left paddle miss
    if ball.xcor() < -400:
        ball.reset()
        scoreboard.point_r()


    screen.update()


screen.exitonclick()
