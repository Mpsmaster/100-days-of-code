from turtle import Turtle, Screen


screen = Screen()
screen.setup(500, 500)

tim = Turtle("turtle")
tim.penup()
tim.color("blue")
tim.goto(-230, 0)

tom = Turtle("turtle")
tom.penup()
tom.color("red")
tom.goto(-230, 40)

tel = Turtle("turtle")
tel.penup()
tel.color("black")
tel.goto(-230, 80)

tud = Turtle("turtle")
tud.penup()
tud.color("yellow")
tud.goto(-230, 120)

tod = Turtle("turtle")
tod.penup()
tod.color("purple")
tod.goto(-230, -40)

tif = Turtle("turtle")
tif.penup()
tif.color("green")
tif.goto(-230, -80)

tof = Turtle("turtle")
tof.penup()
tof.color("orange")
tof.goto(-230, -120)






screen.exitonclick()