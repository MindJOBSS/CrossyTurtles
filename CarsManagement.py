from turtle import *                 # Import all functions and classes from the turtle module for graphics
from random import choice            # Import choice to randomly select colors and Y-coordinates

# Constants for car properties and movement
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]  # List of possible car colors
MOVE_DISTANCE = 5                   # Initial distance each car moves per update
MOVE_INCREMENT = 10                 # Increment value to increase car speed over time
Y_COORDINATES = list(range(-250, 251, 20))  # List of possible Y-coordinates for car placement

# Car management class to handle car creation, movement, and speed
class Cars_Management:
    def __init__(self):
        self.all_cars = []           # List to store all car objects
        self.x_coordinate = 300      # Initial x-coordinate for car starting position (off-screen)
        self.create_car()            # Call to create the first car upon initialization

    # Method to create a new car
    def create_car(self):
        car = Turtle("square")       # Create a car as a square-shaped turtle
        car.color(choice(COLORS))    # Randomly assign a color to the car
        car.penup()                  # Lift the pen to prevent drawing lines as the car moves
        car.shapesize(stretch_wid=1, stretch_len=2)  # Stretch car to be rectangular (wider shape)
        car.goto(self.x_coordinate, choice(Y_COORDINATES))  # Set initial position with random Y-coordinate
        self.all_cars.append(car)    # Add car to the list of all cars

    # Method to move all cars on the screen
    def cars_move(self):
        for car in self.all_cars:
            car.goto(car.xcor() - MOVE_DISTANCE, car.ycor())  # Move each car left by MOVE_DISTANCE

    # Method to increase the movement speed of cars
    def increment_speed(self):
        global MOVE_DISTANCE
        MOVE_DISTANCE += MOVE_INCREMENT  # Increase the speed of cars by adding MOVE_INCREMENT





    
