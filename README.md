# Snake Game

A classic Snake game developed with Python and Pygame, featuring customizable difficulty levels, a start screen with a snake image, and sound effects.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Code Structure](#code-structure)
- [Contributing](#contributing)

## Features

- **Start Screen**: Displays a "Start" button and a "Difficulty" button to select game speed.
- **Customizable Difficulty**: Choose from "Hard," "Normal," or "Easy" levels to adjust game speed.
- **Snake Growth**: The snake grows longer with each food item it eats.
- **Score Display**: The game shows the current score on the screen.
- **Game Over Screen**: Displays the last score and returns to the start screen.
- **Sound Effects**: Includes sound effects for eating food and hitting the wall or self.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/snake-game.git
   cd snake-game
2. **Install Dependencies**: Make sure Python is installed, then install Pygame:
   ```bash
   pip install pygame
3. Add resources: Ensure that duck.wav, chip.wav (for sound effects), and snake.png (for the snake image) are located in the same directory as the game script.
4. ** Run the game **:
   ```bash
   python snake_game.py

# How to Play

1. **Start the Game**: Click "Start" on the start screen.
2. **Set Difficulty**: Click "Difficulty" on the start screen and choose the level.
3. **Control the Snake**:
   - Use Arrow Keys to navigate the snake: Right, Left, Up, and Down.
   - Avoid hitting the walls or the snake's own body.
4. **Goal**: Eat the red food to score points and grow the snake.

# Code Structure

## Main Components

### Class SnakeGame
Contains all methods for the game's functionality, screen rendering, and gameplay logic.

#### Methods:

- `__init__()`: Initializes screen, assets, variables, and sets default values.
- `generate_food_position()`: Randomly generates a new position for food.
- `show_score()`: Displays the player's current score on the screen.
- `reset_game()`: Resets game variables after game over.
- `handle_key_event()`: Processes key events for snake direction.
- `update_direction()`: Updates the direction of the snake based on player input.
- `update_snake_position()`: Moves the snake and grows it if food is eaten.
- `check_food_collision()`: Checks if the snake head has collided with food and increases score.
- `spawn_food()`: Spawns new food after it has been eaten.
- `check_wall_collision()`: Ends the game if the snake collides with the wall.
- `check_self_collision()`: Ends the game if the snake collides with itself.
- `show_start_screen()`: Displays start and difficulty buttons, along with the snake image.
- `set_difficulty()`: Provides options for setting the game’s difficulty level.
- `show_game_over_screen()`: Displays the final score and a Game Over message.

## Game Flow:
The `run_game()` method controls the main game loop. The game alternates between the start screen, game loop, and game over screen based on player actions.

## Global Variables

### Constants:
- Define colors, screen width/height, etc.
  
### Assets:
- Paths for audio files and images.

### Game State Variables:
- `snake_pos`: Initial position of the snake's head.
- `snake_body`: List of segments making up the snake.
- `food_pos`: Randomized position of food.
- `direction` & `change_to`: Manage movement direction.
- `score`: Tracks player’s score.
- `difficulty`: Adjusts game speed based on selected level.

# Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request. Contributions such as bug fixes, additional features, and improvements to the code are welcome!

