from turtle import *                  # Import all functions and classes from the turtle module for graphics

# Constants for player settings and finish line
STARTING_POSITION = (0, -280)         # Player's starting position at the bottom center of the screen
MOVE_DISTANCE = 15                    # Distance the player moves with each upward movement
FINISH_LINE_Y = 270                   # Y-coordinate representing the finish line

# Player class to handle player movement and position
class Player(Turtle):
    def __init__(self):
        super().__init__()            # Initialize the parent Turtle class
        self.shape("turtle")          # Set the player's shape to a turtle
        self.penup()                  # Lift pen to prevent drawing lines when moving
        self.setheading(90)           # Set the turtle to face upward (90 degrees)
        self.reset_origin()           # Move player to starting position

    # Method to move the player up the screen
    def move_up(self):
        if self.ycor() < FINISH_LINE_Y:  # Check if player is below the finish line
            self.forward(MOVE_DISTANCE)  # Move player forward (upward) by MOVE_DISTANCE

    # Method to reset player position to the starting point
    def reset_origin(self):
        self.goto(STARTING_POSITION)   # Set the player position to the starting coordinates

    # Method to check if player has reached the top of the screen (finish line)
    def player_at_top(self):
        return self.ycor() > FINISH_LINE_Y  # Return True if player's y-coordinate is past the finish line
