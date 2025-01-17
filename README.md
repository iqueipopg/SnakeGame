![Snake Game Banner](SnakeGame_Banner.png)

# Snake Game 🐍🎮

**Snake Game** is a Python-based version of the classic Snake game where the player controls a snake that aims to consume apples. Unlike traditional versions, this game introduces new types of apples that trigger different events during gameplay. Developed as part of a **First Year Programming Project** for the **Bachelor's Degree in Mathematical Engineering and Artificial Intelligence** at **Universidad Pontificia Comillas, ICAI**.

## 📜 Table of Contents
- [📌 Project Overview](#-project-overview)
- [🛠️ Installation](#️-installation)
- [🎮 How to Play](#-how-to-play)
- [📂 Project Structure](#-project-structure)
- [🖥️ Technologies Used](#-technologies-used)
- [🙌 Credits](#-credits)

## 📌 Project Overview

Snake Game allows users to:
- **Control a snake** to eat apples and grow in size.
- **Different types of apples** trigger various events, adding a unique twist to the gameplay.
- **Win the game** by collecting 50 points or **lose** by hitting the borders or eating purple apples.
- Includes a **start screen** and **instructions** to guide the player.

## 🛠️ Installation

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/iqueipopg/SnakeGame.git
```

### 2️⃣ Run the Application
```sh
python src/main.py
```

## 🎮 How to Play

### 🐍 Snake Mechanics
- The player controls the snake using the arrow keys. The snake moves in the selected direction and grows in length when it consumes apples.
- The game ends if the snake hits the border or consumes a **purple apple**, which causes the game to end in a loss.

### 🍏 Apple Types
- **Red Apples**: These are standard apples that add points to the player’s score when consumed.
- **Purple Apples**: These special apples cause the snake to lose the game if eaten.
- **Golden Apples**: These special apples cause the player to win 3 points instead of 1.
- **Blue Apples**: These special apples cause the snake move slower for a period of time, making it easier to play.

### 🏆 Victory & Defeat
- **Victory**: The game ends when the player collects 50 points. A victory screen is displayed when this happens.
- **Defeat**: If the snake hits the screen border or eats a purple apple, a defeat screen is shown.

### 🎶 Sound Effects
- Various sound effects are triggered during gameplay, such as:
  - Eating an apple
  - Losing the game
  - Winning the game

## 📂 Project Structure

```plaintext
C:.
├───extras
│   └───sonidos               # Folder containing sound files
├───src                        # Source code
│   ├───__pycache__           # Python cache files (ignored)
│   ├── funciones.py          # Contains game logic functions
│   ├── main.py               # Main script to start the game
│   ├── test.py               # Test cases for game functionality
│   ├── objetos.py            # Defines game objects like the snake and apples
└───__pycache__               # Python cache files (ignored)
```

## 🖥️ Technologies Used

### 🔧 Development
- **Python** – The core programming language used to develop the game.
- **pygame** – A library used for game development, rendering graphics, and handling user inputs.

### 🎮 Game Logic
- **random** – Used to randomly place apples on the screen at different positions.

### 🎶 Audio
- **pygame.mixer** – A module from pygame used to manage sound effects during gameplay, such as when the snake eats an apple or when the game ends.


## 🙌 Credits

This project was developed as part of a **Programming course** in the **Bachelor's Degree in Mathematical Engineering and Artificial Intelligence** at **Universidad Pontificia Comillas, ICAI**.

### 🎓 Special Thanks To:
- **Professors and mentors** for their guidance and support throughout the development of this project.
- **Universidad Pontificia Comillas, ICAI** for providing an excellent learning environment.

### 👨‍💻 Developer:
- **Ignacio Queipo de Llano Pérez-Gascón**

Thanks to all **open-source contributors** and the creators of **pygame** for making this project possible. 🚀
