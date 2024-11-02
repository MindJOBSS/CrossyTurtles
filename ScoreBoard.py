FONT = ("Courier", 20, "normal")      # Font style for displaying the level
FONT2 = ("Courier", 26, "normal")     # Font style for displaying "GAME OVER" message
from turtle import Turtle             # Import the Turtle class for creating scoreboard functionality

# ScoreBoard class to manage level display and game over message
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()            # Initialize the parent Turtle class
        self.shape("arrow")           # Set shape to arrow (optional, since it's hidden)
        self.hideturtle()             # Hide the turtle cursor
        self.penup()                  # Lift pen to prevent drawing lines
        self.goto(-290, 260)          # Set initial position for displaying level score
        self.level = 1                # Initialize the starting level
        self.show_score()             # Display the initial score

    # Method to display the current level on the screen
    def show_score(self):
        self.clear()                  # Clear previous score display
        self.write(f"Level: {self.level}", align="left", font=FONT)  # Write the current level

    # Method to increment the level score by 1
    def score_increment(self):
        self.level += 1               # Increase the level by 1

    # Method to display "GAME OVER" message when game ends
    def game_over(self):
        self.goto(0, 0)               # Move to the center of the screen
        self.write("GAME OVER", align="center", font=FONT2)  # Display game over message
