import time
from turtle import Turtle, Screen
from paddle import Paddle
import turtle
from ball import Ball
from scoreboard import Scoreboard


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
screen = Screen()
score = Scoreboard()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong-Game")
game_is_on = True
turtle.listen()
turtle.onkey(r_paddle.up, key="Up")
turtle.onkey(r_paddle.down, key="Down")
turtle.onkey(l_paddle.up, key="w")
turtle.onkey(l_paddle.down, key="s")
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # Detect collison with wall

    if ball.ycor() > 282 or ball.ycor() < -282:
        # needs to bounce
        ball.bounce_y()
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
