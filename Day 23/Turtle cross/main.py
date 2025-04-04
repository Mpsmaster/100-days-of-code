from turtle import Turtle, Screen
from scoreboard import Scoreboard
from player import Player
from cars import Cars
import time



screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)

player = Player()
cars = Cars()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_in_on = True

while game_in_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_cars()
    scoreboard.actual_level()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_in_on = False
            scoreboard.game_over()

    if player.is_on_finish_line():
        player.go_to_start()
        cars.speedup()
        scoreboard.score_up()














screen.exitonclick()

