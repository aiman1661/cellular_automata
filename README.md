# Cellular Automata Simulations

This repository contains implementations of two different cellular automata models:

1. **SIRS** (Susceptible-Infected-Recovered-Susceptible) - An epidemiological model
2. **Game of Life** - Conway's classic cellular automaton

## SIRS Model

The SIRS model simulates the spread of disease through a population where individuals transition between three states:
- **S (Susceptible)**: Can become infected (value 0)
- **I (Infected)**: Currently infected and can spread to others (value -1)
- **R (Recovered)**: Temporary immunity after infection (value 1)
- **Immune**: Optional permanent immune state (value 2)

### Files

- `SIRS_functions.py`: Core functions for the SIRS model
- `SIRS_class.py`: Object-oriented wrapper for SIRS functionality
- `SIRS_simulation.py`: Run simulations with varying p1 and p3 parameters
- `SIRS_immune_sim.py`: Investigate effects of immune population fraction
- `SIRS_waves_search.py`: Search for wave patterns by calculating infection variance

### Visualisation Notebooks
- `SIRS_Visualisation.ipynb`: Visualisation of system dynamics, real-time plots
- `SIRS_analysis.ipynb`: Data analysis of simulation results

Datafiles are included -- to be used with the analysis notebook.

### Parameters

- **p1**: Probability of S → I transition when near infected sites
- **p2**: Probability of I → R transition
- **p3**: Probability of R → S transition

`.png` files are included for sample plots of results.

## Game of Life

Conway's Game of Life is a cellular automaton with simple rules that lead to complex emergent behavior.

### Files

- `GameOfLife_functions.py`: Core functions for Game of Life
- `GameOfLife_class.py`: Object-oriented wrapper for Game of Life
- `GameOfLife_Simulation.py`: Run simulations to measure equilibrium times

### Visualisation Notebooks
- `GameOfLife_Visualisation.ipynb`: Visualisation of system dynamics, real-time plots
- `GameOfLife_Analysis.ipynb`: Data analysis of simulation results

Datafiles are included -- to be used with the analysis notebook.

### Patterns

Several pre-defined patterns are included:
- Glider
- Blinker
- Beehive
- Flower
- Crab

`.png` files are included for sample plots of results.

## Usage

Run simulations from the command line:

```bash
# running an example simulation script
nohup python SIRS_simulation.py <iterations> <resolution> <output .npy file name> > <output file> &

# Example:
nohup python SIRS_simulation.py 1100 0.05 measurements > measurements.txt &
```

## Analysis

Simulation results are saved as NumPy (.npy) files that can be loaded for analysis:

```python
import numpy as np
data = np.load('measurements.npy', allow_pickle=True).item()
```

## Requirements
- Numpy
- Matplotlib for visualisation
- pandas for data handling (optional)
