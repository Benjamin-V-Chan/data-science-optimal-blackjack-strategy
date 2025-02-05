# data-science-optimal-blackjack-strategy

# Project Overview

This project simulates **Blackjack** and analyzes different (basic, automated-sum, random-replacement) stop strategies to determine their impact on player success. Blackjack is a popular probability-based card game where the goal is to get as close to **21** as possible without exceeding it.

## Folder Structure

```
project-root/
├── scripts/
│   ├── 01_generate_data.py       # Simulate Blackjack games
│   ├── 02_analyze_data.py        # Compute statistics
│   ├── 03_visualize_results.py   # Graph the outcomes
├── outputs/                      # Stores results
│   ├── simulation_results.csv    # Raw simulation data
│   ├── analysis_summary.json     # Statistical summary
│   ├── visualizations/           # Plots
├── requirements.txt               # Dependencies
├── README.md                      # Documentation
```

## Usage

### 1. Setup the Project:

```sh
# Clone the repository
# Ensure you have Python installed
# Install required dependencies
pip install -r requirements.txt
```

### 2. Run Blackjack Simulation

```sh
python scripts/01_generate_data.py --games 10000 --strategy "stop_at_17"
```

This generates game data for **10,000** games using the "stop at 17" strategy.

### 3. Analyze the Simulation Data

```sh
python scripts/02_analyze_data.py
```

This computes win/loss probabilities and expected values.

### 4. Visualize Results

```sh
python scripts/03_visualize_results.py
```

This generates visualizations of strategy performance.

## Requirements

- Python 3.8+
- NumPy
- Pandas
- Matplotlib