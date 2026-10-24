# Shape Catcher Game

An interactive arcade-style game built in Python using the `turtle` graphics library and Object-Oriented Programming (OOP) principles. Random shapes fall from the top of the screen, and the player moves a paddle to catch them. Each shape has a different effect on the score.

---

## Project Architecture

* **main.py** — Screen setup, keyboard controls, and the main game loop (catch detection and speed increase)
* **ball.py** — `Ball` class: the falling shape, with random shape, color, size, and starting position
* **paddle.py** — `Paddle` class: the player's paddle, moving left and right inside the screen edges
* **score.py** — `Scoreboard` class: shows the score, adds points, resets the score, and shows Game Over
* **README.md** — Project documentation

---

## Game Controls

* **Left Arrow:** Move Paddle Left
* **Right Arrow:** Move Paddle Right

---

## Game Rules

| Shape | Effect |
|---|---|
| Circle | +1 point |
| Square | +2 points |
| Colored turtle | +5 points |
| Triangle | Score resets to 0 |
| White turtle | Game Over |

* Missed shapes simply respawn at the top.
* The game gets faster by 10% after every catch.

---

## Key Features

* **OOP Architecture:** Separate classes for `Ball`, `Paddle`, and `Scoreboard`, each in its own file.
* **Random Spawning:** Every new shape gets a random type, color, size, and x position using the `random` module.
* **Increasing Difficulty:** The game loop delay is multiplied by 0.9 after each catch.
* **Distance-Based Collision:** Uses `distance()` and the shape's y position to detect a catch.

---

## Setup & Execution

1. **Clone the repository:**
   `git clone https://github.com/nepal-aly/shape-catcher-game.git`

2. **Navigate to directory:**
   `cd shape-catcher-game`

3. **Run the application:**
   `python main.py`
