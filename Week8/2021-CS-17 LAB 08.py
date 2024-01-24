import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.current_player = 'X' if self.current_player == 'O' else 'O'
        else:
            raise ValueError("Invalid move")

    def is_winner(self, player):
        # Check if 'player' has won the game
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if all(self.board[i] == player for i in combo):
                return True
        return False

    def is_draw(self):
        # Check if the game is a draw
        return ' ' not in self.board

    def display_board(self):
        # Display the current state of the board
        for i in range(0, 9, 3):
            print(" | ".join(self.board[i:i+3]))
            if i < 6:
                print("---------")

class MonteCarloAgent:
    def __init__(self, epsilon=0.1):
        self.value_function = {}  # Store state values
        self.epsilon = epsilon  # Exploration rate

    # Rest of your class implementation...

    def select_move(self, game):
        if random.random() < self.epsilon:
            # Explore: choose a random valid move
            valid_moves = [i for i, cell in enumerate(game.board) if cell == ' ']
            return random.choice(valid_moves)
        else:
            # Exploit: choose the move with the highest value
            valid_moves = [i for i, cell in enumerate(game.board) if cell == ' ']
            values = [self.value_function.get(tuple(game.board[:i] + [game.current_player] + game.board[i+1:]), 0) for i in valid_moves]
            best_move = valid_moves[values.index(max(values))]
            return best_move

    def update_value_function(self, game_history, reward):
        for state in game_history:
            if state not in self.value_function:
                self.value_function[state] = 0
            self.value_function[state] += reward

def train(agent, episodes):
    for episode in range(episodes):
        game = TicTacToe()
        game_history = []
        while not game.is_winner('X') and not game.is_winner('O') and not game.is_draw():
            state = tuple(game.board)
            game_history.append(state)
            move = agent.select_move(game)
            game.make_move(move)
            print(f"Episode {episode + 1}, Step {len(game_history):2}: Player {game.current_player}, Move {move}")
            game.display_board()
        if game.is_winner('X'):
            agent.update_value_function(game_history, 1)
            print("Player X wins!")
        elif game.is_winner('O'):
            agent.update_value_function(game_history, -1)
            print("Player O wins!")
        else:
            agent.update_value_function(game_history, 0)
            print("It's a draw!")

def evaluate(agent, opponents, num_episodes):
    results = {}
    for opponent in opponents:
        wins = 0
        for episode in range(num_episodes):
            game = TicTacToe()
            print(f"Evaluation Episode {episode + 1} - {agent._class.__name} vs. {opponent.__class.__name_}")
            game.display_board()
            while not game.is_winner('X') and not game.is_winner('O') and not game.is_draw():
                if game.current_player == 'X':
                    move = agent.select_move(game)
                else:
                    move = opponent.select_move(game)
                game.make_move(move)
                game.display_board()
            if game.is_winner('X'):
                wins += 1
                print(f"{agent._class.__name_} wins!")
            elif game.is_winner('O'):
                print(f"{opponent._class.__name_} wins!")
            else:
                print("It's a draw!")
        results[opponent._class.__name_] = wins
    return results

# Example usage:
if __name__ == "__main__":
    agent = MonteCarloAgent(epsilon=0.1)
    train(agent, episodes=100)
    opponents = [MonteCarloAgent(epsilon=0.1), MonteCarloAgent(epsilon=0.2)]  # You can add different opponents
    evaluation_results = evaluate(agent, opponents, num_episodes=5)
    print("\nEvaluation Results:")
    for opponent, wins in evaluation_results.items():
        print(f"{opponent}: {wins} wins")


# # -*- coding: utf-8 -*-
# """
# Created on Sat Oct 28 19:24:39 2023

# @author: Administrator
# """

# import numpy as np
# import gym

# # Create the FrozenLake environment
# env = gym.make('FrozenLake-v1', is_slippery=True)  # 'is_slippery' introduces the stochasticity

# # Define MDP parameters
# num_states = env.observation_space.n
# num_actions = env.action_space.n
# gamma = 0.99  # Discount factor

# # Initialize the value function and policy
# value_function = np.zeros(num_states)
# policy = np.zeros(num_states, dtype=int)

# # Define the reward function
# def reward_function(state, action, next_state):
#     if state == next_state:
#         return 0.0  # No change in state, no reward
#     if next_state == env.nS - 1:  # Reached the goal
#         return 1.0
#     if next_state in env.env.desc.ravel() == b'H':  # Fell into a hole
#         return -1.0
#     return -0.1  # Small negative reward for other transitions

# # Value Iteration algorithm
# def value_iteration():
#     num_iterations = 1000
#     for i in range(num_iterations):
#         new_value_function = np.zeros(num_states)
#         for state in range(num_states):
#             expected_rewards = []
#             for action in range(num_actions):
#                 expected_reward = 0
#                 for prob, next_state, _, _ in env.P[state][action]:
#                     expected_reward += prob * (reward_function(state, action, next_state) + gamma * value_function[next_state])
#                 expected_rewards.append(expected_reward)
#             new_value_function[state] = max(expected_rewards)
#         value_function = new_value_function
#     return value_function

# # Policy extraction from value function
# def extract_policy(value_function):
#     for state in range(num_states):
#         q_values = []
#         for action in range(num_actions):
#             q_value = 0
#             for prob, next_state, _, _ in env.P[state][action]:
#                 q_value += prob * (reward_function(state, action, next_state) + gamma * value_function[next_state])
#             q_values.append(q_value)
#         policy[state] = np.argmax(q_values)

# # Solve the Frozen Lake problem
# value_function = value_iteration()
# extract_policy(value_function)

# # Display the optimal policy
# print("Optimal Policy:")
# policy_symbols = ['L', 'D', 'R', 'U']  # Left, Down, Right, Up
# for state in range(num_states):
#     print(f'State {state}: Move {policy_symbols[policy[state]]}')

# # Run a simulation with the optimal policy
# state = env.reset()
# env.render()
# done = False
# while not done:
#     action = policy[state]
#     state, _, done, _ = env.step(action)
#     env.render()
