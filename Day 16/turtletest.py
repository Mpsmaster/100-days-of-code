# import turtle
# timmy = turtle.Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("blue2")
# timmy.forward(100)
# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Squartle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "r"
print(table)
