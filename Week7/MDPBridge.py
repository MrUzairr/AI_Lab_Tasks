import numpy as np

class FrozenLakeMDP:
    def __init__(self, gridworld):
        self.gridworld = gridworld
        self.state_space = set(range(len(gridworld)))
        self.action_space = set(['UP', 'DOWN', 'LEFT', 'RIGHT'])
        self.transition_probabilities = {}
        self.reward_function = {}

        for state in self.state_space:
            for action in self.action_space:
                self.transition_probabilities[(state, action)] = {}

        for state in self.state_space:
            for action in self.action_space:
                next_state = self.gridworld[(state, action)]
                self.transition_probabilities[(state, action)][next_state] = 0.75
                for other_next_state in self.state_space:
                    if other_next_state != next_state:
                        self.transition_probabilities[(state, action)][other_next_state] = 0.25 / 3

        for state in self.state_space:
            for action in self.action_space:
                next_state = self.gridworld[(state, action)]
                if next_state == 'G':
                    self.reward_function[(state, action)] = 1.0
                else:
                    self.reward_function[(state, action)] = 0.0

    def value_iteration(self, gamma=0.9):
        value_function = np.zeros(len(self.state_space))
        while True:
            delta = 0.0
            for state in self.state_space:
                for action in self.action_space:
                    q_value = 0.0
                    for next_state, probability in self.transition_probabilities[(state, action)].items():
                        q_value += probability * (self.reward_function[(state, action)] + gamma * value_function[next_state])

                    new_value_function = max(q_value, value_function[state])
                    delta = max(delta, abs(new_value_function - value_function[state]))
                    value_function[state] = new_value_function

            if delta < 1e-6:
                break

        return value_function

    def extract_policy(self, value_function):
        policy = {}
        for state in self.state_space:
            best_action = None
            max_q_value = float('-inf')
            for action in self.action_space:
                q_value = 0.0
                for next_state, probability in self.transition_probabilities[(state, action)].items():
                    q_value += probability * (self.reward_function[(state, action)] + gamma * value_function[next_state])

                if q_value > max_q_value:
                    best_action = action
                    max_q_value = q_value

            policy[state] = best_action

        return policy

if __name__ == '__main__':
    gridworld = {
        (0, 'UP'): 0, (0, 'DOWN'): 4, (0, 'LEFT'): 0, (0, 'RIGHT'): 1,
        (1, 'UP'): 0, (1, 'DOWN'): 5, (1, 'LEFT'): 0, (1, 'RIGHT'): 2,
        (2, 'UP'): 1, (2, 'DOWN'): 6, (2, 'LEFT'): 1, (2, 'RIGHT'): 3,
        (3, 'UP'): 2, (3, 'DOWN'): 7, (3, 'LEFT'): 3, (3, 'RIGHT'): 'G',
    }

    mdp = FrozenLakeMDP(gridworld)

    value_function = mdp.value_iteration()

    policy = mdp.extract_policy(value_function)

    print('Optimal policy:')
    for state, action in policy.items():
        print(f'{state}: {action}')
