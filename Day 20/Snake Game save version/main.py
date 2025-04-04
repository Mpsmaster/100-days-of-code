from scoreboard import Scoreboard
from turtle import Screen
from snake import Snake
from food import Food
import time
try:
    with open("high_score.txt", "r") as file:
        content = file.read().strip()
        high_score = int(content) if content else 0
except (FileNotFoundError, ValueError):
    high_score = 0

def setup_game():
    global snake, food, scoreboard, high_score
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    scoreboard.high_score = high_score
    setup_controls()
    setup_screen()
    scoreboard.update_score()

def setup_controls():  
    global screen
    screen = Screen()  
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

def setup_screen():
    global screen
    screen = Screen()  
    screen.bgcolor("black")
    screen.title("My snake game")
    screen.setup(width=600, height=600)
    screen.tracer(0)

setup_game()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        
        response = screen.textinput("Do you want to play again?", "yes or no")
        if response.lower() == "yes":
            if scoreboard.score > high_score:
                high_score = scoreboard.score
            with open("high_score.txt", "w") as file:
                file.write(str(high_score))    
            screen.clearscreen()
            setup_game()
            scoreboard.reset_score()
            snake.reset_snake()
            game_is_on = True
        else:
            if scoreboard.score > high_score:
                high_score = scoreboard.score
            scoreboard.high_score = high_score
            with open("high_score.txt", "w") as file:
                file.write(str(high_score))
            scoreboard.reset_score()    
            game_is_on = False
            scoreboard.game_over()    
        

    for square in snake.squares[1:]:
        if snake.head.distance(square) < 10:
            
            response = screen.textinput("Do you want to play again?", "yes or no")
            if response.lower() == "yes":
                if scoreboard.score > high_score:
                    high_score = scoreboard.score
                with open("high_score.txt", "w") as file:
                    file.write(str(high_score))    
                screen.clearscreen()
                setup_game()
                scoreboard.reset_score()
                snake.reset_snake()
                game_is_on = True
            else:
                if scoreboard.score > high_score:
                    high_score = scoreboard.score
                scoreboard.high_score = high_score
                with open("high_score.txt", "w") as file:
                    file.write(str(high_score))     
                scoreboard.reset_score()      
                game_is_on = False
                scoreboard.game_over()     
        



        

screen.exitonclick()