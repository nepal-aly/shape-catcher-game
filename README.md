# Shape Catcher Game 🎮

An interactive arcade-style game built in Python using the `turtle` graphics library and Object-Oriented Programming (OOP) principles.

---

## 🏗️ Project Architecture

* **main.py** — Core game loop & event management
* **catcher.py** — Player basket/catcher object & movement
* **shapes.py** — Shape generation, falling logic, & collisions
* **scoreboard.py** — Live score, lives visualizer, & Game Over UI
* **README.md** — Project documentation

---

## 🎮 Game Controls

* **Left Arrow:** Move Catcher Left
* **Right Arrow:** Move Catcher Right

---

## 🌟 Key Features

* **OOP Architecture:** Clean separation of concerns across multiple modules (`Catcher`, `Shapes`, `Scoreboard`).
* **Dynamic Physics & Spawning:** Random shape generation with incremental speed scaling to increase difficulty.
* **Collision Engine:** Precision boundary and distance detection for successful catches vs. missed drops.
* **Lives & Score System:** Real-time visual tracking of remaining attempts and persistent score counter.

---

## 🛠️ Setup & Execution

1. **Clone the repository:**
   `git clone https://github.com/nepal-aly/shape-catcher-game.git`

2. **Navigate to directory:**
   `cd shape-catcher-game`

3. **Run the application:**
   `python main.py`
