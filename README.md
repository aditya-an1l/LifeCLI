<div align="center">
  <img alt="Logo" src="https://raw.githubusercontent.com/aditya-an1l/LifeCLI/main/media/logo.png" width="50%" height="50%">
<h1><b>LifeCLI</b></h1>
</div>



<div align="center"><p>
    </a>
    <a href="https://github.com/aditya-an1l/LifeCLI/pulse">
      <img alt="Last commit" src="https://img.shields.io/github/last-commit/aditya-an1l/LifeCLI?style=for-the-badge&logo=git&color=fceb79&logoColor=2778e3&labelColor=000000"/>
    </a>
    <a href="https://github.com/aditya-an1l/LifeCLI/blob/main/LICENSE">
      <img alt="License" src="https://img.shields.io/github/license/aditya-an1l/LifeCLI?style=for-the-badge&logo=apache&color=7c675f&logoColor=2778e3&labelColor=000000" />
    </a>
    <a href="https://github.com/aditya-an1l/LifeCLI/stargazers">
      <img alt="Stars" src="https://img.shields.io/github/stars/aditya-an1l/LifeCLI?style=for-the-badge&logo=starship&color=fceb79&logoColor=2778e3&labelColor=000000" />
    </a>
    <a href="https://github.com/aditya-an1l/LifeCLI/issues">
      <img alt="Issues" src="https://img.shields.io/github/issues/aditya-an1l/LifeCLI?style=for-the-badge&logo=gitbook&color=7c675f&logoColor=2778e3&labelColor=000000" />
    </a>
    <a href="https://github.com/aditya-an1l/LifeCLI">
      <img alt="Repo Size" src="https://img.shields.io/github/repo-size/aditya-an1l/LifeCLI?color=fceb79&label=SIZE&logo=files&style=for-the-badge&logoColor=2778e3&labelColor=000000" />
    </a>
    <a href="https://twitter.com/intent/follow?screen_name=aditya_an1l">
      <img alt="follow on X" src="https://img.shields.io/twitter/follow/aditya_an1l?style=for-the-badge&logo=x&color=ffffff&logoColor=2778e3&labelColor=000000" />
    </a>

</div>

# Conway's Game of Life

A dynamic terminal-based implementation of **Conway's Game of Life**, written in Python.

![preview](https://raw.githubusercontent.com/aditya-an1l/LifeCLI/main/media/preview.gif)

## 🧠 What is LifeCLI: A Conway's Game of Life Simulation

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
├── media/              # media files
├── .gitignore
├── gof.py              # Main script

```

----------

## 📜 License

This project is released under the MIT License.
