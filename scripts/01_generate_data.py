import random
import csv
import os

OUTPUT_FILE = "outputs/simulation_results.csv"

def deal_card():
    """Returns a random card from a standard deck."""
    card = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11])  # Face cards = 10, Ace = 11
    return card

def hand_value(hand):
    """Calculates hand value, treating Ace as 1 or 11 optimally."""
    total = sum(hand)
    ace_count = hand.count(11)
    
    while total > 21 and ace_count:
        total -= 10  # Convert an Ace from 11 to 1
        ace_count -= 1
    return total

def dealer_play():
    """Dealer follows Blackjack rules (hits until at least 17)."""
    hand = [deal_card(), deal_card()]
    while hand_value(hand) < 17:
        hand.append(deal_card())
    return hand_value(hand)

def player_play(strategy):
    """Simulates the player’s game based on the selected strategy."""
    hand = [deal_card(), deal_card()]
    
    if strategy == "stop_at_17":
        while hand_value(hand) < 17:
            hand.append(deal_card())

    elif strategy == "stop_at_19":
        while hand_value(hand) < 19:
            hand.append(deal_card())

    elif strategy == "mimic_dealer":
        while hand_value(hand) < 17:
            hand.append(deal_card())

    elif strategy == "basic_strategy":
        while hand_value(hand) < 12:  # Always hit below 12
            hand.append(deal_card())
        if 12 <= hand_value(hand) <= 16:
            if random.random() < 0.5:  # 50% chance to hit
                hand.append(deal_card())

    return hand_value(hand)

def determine_outcome(player_score, dealer_score):
    """Determines the winner of the game."""
    if player_score > 21:
        return "Loss"
    elif dealer_score > 21 or player_score > dealer_score:
        return "Win"
    elif player_score == dealer_score:
        return "Tie"
    return "Loss"

def run_simulation(num_games=10000, strategy="stop_at_17"):
    """Runs multiple Blackjack games and records results."""
    results = []

    for _ in range(num_games):
        player_score = player_play(strategy)
        dealer_score = dealer_play()
        outcome = determine_outcome(player_score, dealer_score)
        results.append([outcome, player_score, dealer_score, strategy])

    os.makedirs("outputs", exist_ok=True)
    with open(OUTPUT_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Outcome", "PlayerScore", "DealerScore", "Strategy"])
        writer.writerows(results)

if __name__ == "__main__":
    run_simulation(num_games=10000, strategy="stop_at_17")