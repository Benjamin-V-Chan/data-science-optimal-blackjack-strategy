# Import necessary libraries
# Define a function simulate_game that runs a single St. Petersburg game:
#     - Initialize prize = 1
#     - Flip a fair coin until tails appears
#     - Double the prize each time a heads appears
#     - Return the final prize amount

# Define a function run_simulation that runs multiple games:
#     - Input parameters: number of games to run, betting strategy
#     - Create an empty list to store results
#     - Loop for each game:
#         - Run simulate_game
#         - Apply the given betting strategy (e.g., stopping conditions, fixed bets)
#         - Store the result in a list
#     - Save results to a CSV file in outputs/

# Allow command-line execution where user inputs number of games and strategy