from turtle import Turtle, Screen
MOVEMENT = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
         self.squares = []
         self.create_snake()
         self.head = self.squares[0]

    def create_snake(self):
        for i in range(3):
            self.add_square(i)
            

    def add_square(self, position):
        new_squares = Turtle("square")
        new_squares.color("white")
        new_squares.penup()
        if isinstance(position, int):
            new_squares.goto(0 - 20 * position, 0)
        else:
            new_squares.goto(position)    
        self.squares.append(new_squares)

    def extend(self):  
        self.add_square(self.squares[-1].position())                           

    def move(self):
    
            for seg in range(len(self.squares) - 1, 0, -1):
                square_x = self.squares[seg - 1].xcor() 
                square_y = self.squares[seg - 1].ycor() 
                self.squares[seg].goto(square_x, square_y)
            self.head.forward(MOVEMENT)    
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT) 

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN) 

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)    

    def reset_snake(self):
        for square in self.squares:
            square.hideturtle()
        self.squares.clear()
        self.create_snake()
        self.head = self.squares[0]           















