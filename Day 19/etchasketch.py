from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_right():
    tim.setheading(0)    # 0 degrees = right
    tim.forward(10)

def move_left():
    tim.setheading(180)  # 180 degrees = left
    tim.forward(10)

def move_up():
    tim.setheading(90)   # 90 degrees = up
    tim.forward(10)

def move_down():
    tim.setheading(270)   # 270 degrees = down
    tim.forward(10)

def move_circle_right():    
    tim.forward(10)    # Move forward a small distance
    tim.right(10)    

def move_circle_left():    
    tim.forward(10)    # Move forward a small distance
    tim.left(10)   

def rotate_left():
    rotate = tim.heading() + 10
    tim.setheading(rotate) 

def rotate_right():
    rotate = tim.heading() - 10
    tim.setheading(rotate)  

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def foward():
    tim.forward(10)                


screen.listen()
screen.onkey(key="d", fun=move_right)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="w", fun=move_up)
screen.onkey(key="s", fun=move_down)
screen.onkey(key="c", fun=move_circle_right)
screen.onkey(key="z", fun=move_circle_left)
screen.onkey(key="e", fun=rotate_right)
screen.onkey(key="q", fun=rotate_left)
screen.onkey(key="f", fun=clear)
screen.onkey(key="r", fun=foward)
screen.exitonclick()