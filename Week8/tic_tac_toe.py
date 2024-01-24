import random

class TicTacToeEnvironment:
    def __init__(self):
        self.board = [[0 for i in range(3)] for j in range(3)]
        self.current_player = 1

    def get_state(self):
        return tuple(tuple(row) for row in self.board)  # Convert to a tuple of tuples

    def is_terminal(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != 0:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != 0:
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            return True

        return False

    def get_reward(self):
        if self.is_terminal():
            if self.current_player == 1:
                return 1
            else:
                return -1
        else:
            return 0

    def take_action(self, action):
        if self.is_terminal() or action < 0 or action > 8:
            return False
        if self.board[action // 3][action % 3] == 0:
            self.board[action // 3][action % 3] = self.current_player
            self.current_player = -self.current_player
            return True
        return False

class MonteCarloAgent:
    def __init__(self):
        self.value_function = {}

    def get_action(self, state):
        state = tuple(state)

        if state not in self.value_function:
            self.value_function[state] = {}

        best_value = -float('inf')
        best_action = None

        for action in range(9):
            if action not in self.value_function[state]:
                self.value_function[state][action] = 0

            value = self.value_function[state][action]
            if value > best_value:
                best_value = value
                best_action = action

        return best_action

    def update_value_function(self, state, action, reward):
        state = tuple(state)

        if state not in self.value_function:
            self.value_function[state] = {}

        if action not in self.value_function[state]:
            self.value_function[state][action] = 0

        self.value_function[state][action] += reward

def simulate_game(agent1, agent2):
    env = TicTacToeEnvironment()

    while not env.is_terminal():
        current_player = env.current_player
        action = agent1.get_action(env.get_state()) if current_player == 1 else agent2.get_action(env.get_state())

        env.take_action(action)

    return env.get_reward()

def train_agent(agent, num_episodes):
    for i in range(num_episodes):
        reward = simulate_game(agent, agent)

        agent.update_value_function(agent.get_state(), agent.get_action(agent.get_state()), reward)

def evaluate_agent(agent, opponent):
    num_wins = 0
    num_losses = 0

    for i in range(100):
        reward = simulate_game(agent, opponent)

        if reward == 1:
            num_wins += 1
        elif reward == -1:
            num_losses += 1

    win_rate = num_wins / (num_wins + num_losses)

    return win_rate

if __name__ == '__main__':
    agent = MonteCarloAgent()

    # Train the agent
    train_agent(agent, 10000)

    # Evaluate the agent against a random opponent
    random_opponent = MonteCarloAgent()
    win_rate = evaluate_agent(agent, random_opponent)

    print('Win rate against random opponent:', win_rate)