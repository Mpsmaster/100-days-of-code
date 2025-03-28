from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


player_r = Paddle(380)
player_l = Paddle(-380)
ball = Ball()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()



key_states = {
    "Up": False,
    "Down": False,
    "s": False,
    "x": False
}

# Key press bindings (set state to True)
screen.onkeypress(lambda: key_states.update({"Up": True}), "Up")
screen.onkeypress(lambda: key_states.update({"Down": True}), "Down")
screen.onkeypress(lambda: key_states.update({"s": True}), "s")
screen.onkeypress(lambda: key_states.update({"x": True}), "x")

# Key release bindings (set state to False)
screen.onkeyrelease(lambda: key_states.update({"Up": False}), "Up")
screen.onkeyrelease(lambda: key_states.update({"Down": False}), "Down")
screen.onkeyrelease(lambda: key_states.update({"s": False}), "s")
screen.onkeyrelease(lambda: key_states.update({"x": False}), "x")


running = True
while running:
    time.sleep(ball.move_speed)

    if key_states["Up"]:
        player_r.go_up()
    if key_states["Down"]:
        player_r.go_down()
    if key_states["s"]:
        player_l.go_up()
    if key_states["x"]:
        player_l.go_down()

    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y() 

    if ball.distance(player_r) < 50 and ball.xcor() > 340 and ball.x_move > 0 or ball.distance(player_l) < 50 and ball.xcor() < -340 and ball.x_move < 0:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position() 
        scoreboard.r_point()            

    screen.update()
























screen.exitonclick()