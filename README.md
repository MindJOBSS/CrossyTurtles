🎮 Crossy Roads: Turtle Edition 🐢

Welcome to Crossy Roads: Turtle Edition – a fun and interactive game built entirely in Python using the Turtle Graphics library! This project is a beginner-friendly game where the player controls a turtle trying to dodge traffic and reach the top of the screen to level up. Here's a breakdown of the game's features and functionality:

🐢 Objective
The goal is simple: guide your turtle from the bottom to the top of the screen without getting hit by any of the moving cars. Each time the turtle reaches the top, the level increases, making the game progressively more challenging by increasing the speed of the cars!

💡 Key Features
Car Management 🚗 – Randomly generated cars of different colors zoom across the screen, adding both challenge and excitement. Cars are controlled by a custom class that handles creation, movement, and speed adjustments as levels increase.
Player Movement 🎮 – The player controls a turtle character that can only move upward. The Turtle Graphics library handles this smoothly with easy-to-use movement functions, making it intuitive to play.
Scoring System 🏆 – Each time the turtle successfully reaches the top, the player’s level increases, displayed on a custom scoreboard. The game gets faster and harder with each level.
Game Over Screen 🚫 – If the turtle collides with any car, the game ends, and a "GAME OVER" message appears.
⚙️ How It Works
The project is split into several custom classes to keep it organized and modular:

Player Class: Handles the turtle character’s movements, starting position, and checks if it reaches the top. The move_up method allows the player to move, while player_at_top resets the turtle once it reaches the goal.
Cars_Management Class: This class generates cars at random intervals and positions, moving them across the screen. It uses Python’s choice function to assign random colors and Y-coordinates, adding variety to each game.
ScoreBoard Class: Manages the display of the player’s current level and shows the "GAME OVER" message upon collision. The scoreboard updates dynamically to reflect the current level.
🔍 Behind the Scenes
Screen Setup: The game uses a 600x600 Turtle Graphics screen, which is refreshed at regular intervals to create smooth animations.
Game Loop: Using a while loop, the game constantly updates the screen, moving cars and checking for collisions, and listens for user input to control the turtle.
Leveling Up: Each time the player reaches the finish line, the level increases, making cars move faster for an added challenge.
🎨 Technology Used
Python 3.x and the Turtle Graphics library for game development
Random module to add unpredictability to car positions and colors
Custom classes to keep the code organized and enhance modularity
🚀 Why This Project?
This game is a great project for anyone learning Python and the Turtle Graphics library. It demonstrates foundational programming concepts like object-oriented programming, screen control, and event handling. Plus, it's a lot of fun to play and see your code in action!
