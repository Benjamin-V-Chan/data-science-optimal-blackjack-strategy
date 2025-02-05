# data-science-optimal-blackjack-strategy

# Project Overview

This project simulates **Blackjack** and analyzes different (basic, automated-sum, random-replacement) stop strategies to determine their impact on player success. Blackjack is a popular probability-based card game where the goal is to get as close to **21** as possible without exceeding it.

## Mathematical Foundation

The game of Blackjack involves probabilistic decision-making and statistical analysis of outcomes. Let’s define key mathematical aspects:

### Probability of Drawing a Specific Card

Each deck has 52 cards. The probability of drawing a specific card is given by:
$$\(P(X = x) = \frac{4}{52} = \frac{1}{13}\)$$
for non-face cards and:
$$\(P(X = 10) = \frac{16}{52} = \frac{4}{13}\)$$
for 10-value cards (10, J, Q, K).

### Expected Value (EV) Calculation

The expected value of a hand given a probability distribution of possible outcomes is:
$$\(EV = \sum_{i=1}^{n} P_i \times X_i\)$$
where $\(P_i\)$ is the probability of obtaining a hand $\(X_i\)$ given a strategy.

For example, for an **initial hand** of **Ace + 10**:
$$\(EV_{blackjack} = P_{blackjack} \times 1.5 - P_{loss} \times 1 - P_{tie} \times 0\)$$

### Dealer Expected Value Under Different Strategies

If the dealer follows the rule of hitting until at least **17**, the probability of them busting can be computed as:
$$\(P_{bust} = \sum_{i=17}^{21} P(\text{dealer reaches } i) \times P(\text{busting from } i)\)$$
This allows for a comparative analysis against player strategies.

### Strategy-Based Expected Value Calculation

The stopping strategy **modifies** the probability of reaching different hand values, affecting the overall expected return. Defining $\(S\)$ as the stopping threshold, the conditional probability of reaching a specific hand value is:
$$\(P(X \geq S) = 1 - \sum_{i=1}^{S-1} P(X = i)\)$$

Thus, different stopping strategies affect:

- **Win probability**: $\(P(X > Y)\)$
- **Loss probability**: $\(P(X < Y)\)$
- **Tie probability**: $\(P(X = Y)\)$

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
- Pandas
- Matplotlib