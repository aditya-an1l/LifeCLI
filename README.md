# Conway's Game of Life

A dynamic terminal-based implementation of **Conway's Game of Life**, written in Python.

## 🧠 What is Conway's Game of Life?

Conway's Game of Life is a **zero-player game** that simulates cellular automata — a grid where cells live, die, or reproduce based on a few simple rules. The patterns evolve with time, often mimicking biological systems.

At each step in time, the following transitions occur:

1.  Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
    
2.  Any live cell with two or three live neighbours lives on to the next generation.
    
3.  Any live cell with more than three live neighbours dies, as if by overpopulation.
    
4.  Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

Source and for information, visit: https://rustwasm.github.io/book/game-of-life/rules.html


## 🚀 Features

- Terminal-based simulation using Python `curses`
- Supports full terminal resizing
- Adjustable cell size and simulation speed
- Keyboard controls for interactivity
- Runs as a CLI screensaver



## 🎮 Controls

| Key        | Action                           |
|------------|----------------------------------|
| `q` / `Esc`| Quit the simulation              |
| `↑`        | Increase cell size               |
| `↓`        | Decrease cell size               |
| `→`        | Increase simulation speed        |
| `←`        | Decrease simulation speed        |



## 🛠️ Installation

### 1. Clone the repository

```sh
git clone https://github.com/aditya-an1l/LifeCLI.git
cd LifeCLI

```

### 2. Run the simulation

```sh
python3 gof.py

```

> 🐧 On Linux, ensure you have the `curses` module (usually preinstalled).  
> 🪟 On Windows, install support via:
> 
> ```sh
> pip install windows-curses
> 
> ```

----------

## 📁 Project Structure

```
LifeCLI/
├── .git/
├── .gitignore
├── gof.py              # Main script

```

----------

## 📜 License

This project is released under the MIT License.
