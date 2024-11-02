from turtle import *                # Import all functions and classes from the turtle module for graphics
from time import sleep              # Import sleep for controlling the game loop speed
from CarsManagement import *        # Import custom CarsManagement module for car creation and management
from Player import *                # Import custom Player module for player movement and interaction
from ScoreBoard import *            # Import custom ScoreBoard module for scoring and game status

# Set up the screen for the game
screen = Screen()
screen.setup(600, 600)              # Set screen dimensions to 600x600 pixels
screen.title("Welcome to Crossy Roads")  # Set the title of the game window
screen.tracer(0)                    # Disable automatic screen updates for smoother animation control

# Initialize game components
cars = Cars_Management()            # Create an instance to manage cars in the game
player = Player()                   # Create an instance for player-controlled character
scoreboard = ScoreBoard()           # Create an instance for displaying score and game status

# Configure user input
screen.listen()                     # Enable screen to listen for user keyboard inputs
screen.onkey(fun=player.move_up, key="Up")  # Bind "Up" arrow key to move the player up

# Define function to exit the game when the screen is clicked
def exit_game(x, y):
    screen.bye()                    # Close the game window
screen.onscreenclick(fun=exit_game, btn=1, add=None)  # Set left mouse click to exit the game

# Game loop variables
game_active = True                  # Boolean variable to keep track of the game's active state
counter = 0                         # Counter variable for controlling car creation frequency

# Main game loop
while game_active:
    sleep(0.1)                      # Slow down the loop for game pacing
    screen.update()                 # Update the screen to reflect any changes

    counter += 1                    # Increment counter on each loop iteration
    if counter == 6:                # Every 6th loop, create a new car
        cars.create_car()           # Generate a new car in the game
        counter = 0                 # Reset counter to control car creation frequency

    cars.cars_move()                # Move all cars on the screen

    # Check if the player reached the top of the screen
    if player.player_at_top():
        player.reset_origin()       # Reset player to starting position
        scoreboard.score_increment() # Increase the player's score
        scoreboard.show_score()     # Display updated score on the screen
        cars.increment_speed()      # Increase car speed to make game progressively harder

    # Detect collision between the player and any car
    for car in cars.all_cars:
        if player.distance(car) < 20:  # If player is within 20 pixels of a car
            game_active = False      # End the game if collision occurs
            scoreboard.game_over()   # Display "Game Over" message on the screen

screen.exitonclick()                 # Wait for user to click to close the window after game ends
