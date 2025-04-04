from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
MOVEMENT_CARS = 10

class Cars:

    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVEMENT_CARS
        

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            random_y = random.randint(-230, 240)
            car.goto(280, random_y)
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def speedup(self):
        self.car_speed += MOVEMENT_CARS