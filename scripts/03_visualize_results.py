import pandas as pd
import matplotlib.pyplot as plt
import os

INPUT_FILE = "outputs/simulation_results.csv"
VISUALIZATION_DIR = "outputs/visualizations/"

def plot_outcomes(df):
    """Plots win/loss/tie percentages per strategy."""
    outcome_counts = df.groupby("Strategy")["Outcome"].value_counts(normalize=True).unstack()
    outcome_counts.plot(kind="bar", stacked=True)
    plt.title("Win/Loss/Tie Percentages by Strategy")
    plt.ylabel("Proportion")
    plt.xlabel("Strategy")
    plt.legend(title="Outcome")
    plt.xticks(rotation=45)
    plt.savefig(f"{VISUALIZATION_DIR}/outcome_distribution.png")
    plt.close()

def plot_boxplot(df):
    """Plots a boxplot of player scores by strategy."""
    df.boxplot(column="PlayerScore", by="Strategy", grid=False)
    plt.title("Player Score Distribution by Strategy")
    plt.xlabel("Strategy")
    plt.ylabel("Final Player Score")
    plt.xticks(rotation=45)
    plt.savefig(f"{VISUALIZATION_DIR}/boxplot.png")
    plt.close()

def visualize_results():
    """Generates plots from simulation data."""
    df = pd.read_csv(INPUT_FILE)

    os.makedirs(VISUALIZATION_DIR, exist_ok=True)
    plot_outcomes(df)
    plot_boxplot(df)

if __name__ == "__main__":
    visualize_results()