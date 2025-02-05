import pandas as pd
import json
import os

INPUT_FILE = "outputs/simulation_results.csv"
OUTPUT_FILE = "outputs/analysis_summary.json"

def analyze_results():
    """Reads simulation data and computes statistics."""
    df = pd.read_csv(INPUT_FILE)
    
    summary = df.groupby("Strategy")["Outcome"].value_counts(normalize=True).unstack().fillna(0)
    summary["average_player_score"] = df.groupby("Strategy")["PlayerScore"].mean()
    
    result_dict = summary.to_dict()

    os.makedirs("outputs", exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(result_dict, f, indent=4)

if __name__ == "__main__":
    analyze_results()