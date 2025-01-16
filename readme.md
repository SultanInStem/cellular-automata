# Cellular Automata Simulation

This project simulates a **Cellular Automaton** with simple rules for cell evolution over time. The simulation runs in a grid, where each cell can be in a state (e.g., alive or dead), and its next state is determined based on its neighbors. The simulation allows you to observe how the grid evolves step by step, following specific rules.

## Demo
![Demo gif](demo.gif)

## Features

- A grid-based cellular automaton that evolves over time.
- Simple rules for cell state changes based on neighboring cells.
- Interactive controls to manage the simulation.

## Controls

- **R**: Reset the simulation. This will clear the grid and restart the automaton.
- **Space**: Pause and resume the simulation. This allows you to stop the evolution and resume it at your convenience.
- **Mouse Click**: make a cell alive but only when the simulation is paused


## How to Run

1. Clone this repository to your local machine.

``` bash 
git clone git@github.com:SultanInStem/cellular-automata.git
``` 

2. Activate env (MacOs)
``` bash 
source env/bin/activate
``` 
2. Activate env (Windows)
``` bash 
.\env\Scripts\activate
```
3. Run the simulation 
``` bash 
python3 main.py
```