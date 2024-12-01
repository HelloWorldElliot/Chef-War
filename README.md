
# Chef War

**Chef War** is a thrilling two-player local mini-game developed using **Pygame**. Set in a dynamic kitchen battleground, players compete as rival chefs in a battle for culinary supremacy. With a secret recipe on the line, the chef who scores the highest across five intense levels will be crowned the ultimate kitchen champion!

---

## Features

- **Local Multiplayer Gameplay**: Two players compete head-to-head in a shared kitchen environment.
- **Five Unique Levels**: Each level brings new challenges and opportunities to earn points.
- **Dynamic Scoring System**: Compete to gather the highest score and claim victory.
- **Independent Production**: From the user interface to the background music, everything has been crafted in-house by the development team.

---

## Requirements

Ensure you have the following installed:

- **Python** (Version 3.6 or later)
- **Pygame** (Install via the instructions below)

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/chef-war.git
   cd chef-war
   ```

2. **Install Dependencies**:
   Use the provided `requirements.txt` file to install all necessary Python packages:
   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` is missing, install Pygame manually:
   ```bash
   pip install pygame
   ```

3. **Run the Game**:
   Launch the game by running the main script:
   ```bash
   python main.py
   ```

---

## How to Play

1. **Objective**: Compete to score the most points by collecting ingredients, completing tasks, and sabotaging your opponent.
2. **Controls**:
   - **Player 1 (Chef 1)**:
     - Move: `W` (up), `A` (left), `S` (down), `D` (right)
     - Action: `Space`
   - **Player 2 (Chef 2)**:
     - Move: Arrow keys
     - Action: `Enter`
3. **Winning**: The chef with the highest score at the end of five levels wins the game!

---

## Project Structure

```
chef-war/
├── assets/
│   ├── images/        # Game sprites and background images
│   ├── music/         # Background music and sound effects
│   ├── font/          # All the fonts using in the game
├── modules/           # Python scripts for game components
│   ├── chef.py        # Logic for chef characters
│   ├── block.py       # Logic for game blocks and objects
│   ├── ...            # Other game modules
├── main.py            # Entry point for the game
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

---

## Development Team

Chef War was independently developed and produced by the team from Colby College: Phuong Nguyen Ngoc, Elliot Zhou, Zixuan Wang, Eduardo Sosa, Katie Andre, Izzy Hurley, handling all aspects of the project, including:

- **Game Development**: Programming and game logic design.
- **Music and Sound**: Custom background tracks and sound effects.
- **UI Design**: Intuitive and fun user interface.


---

## License

This project is licensed under the **MIT License**. Feel free to fork, modify, and share it!

---

## Acknowledgments

Special thanks to the Python and Pygame communities for providing tools and inspiration for game development.
