""" A Markov Decision Process, also known as an MDP model, contains the following set of features:
- A set of possible states, S.
- A set of models.
- A set of possible actions, A.
- A real-valued reward function, R(s, a).
- A solution to the Markov Decision Process.
The Frozen Lake problem is a classic grid-world problem used in reinforcement learning to 
demonstrate and test various algorithms. It's a simple but illustrative problem that involves an agent navigating a grid while facing challenges. Here's a brief description of the Frozen Lake problem:
Environment:
1. The environment is represented as a grid, typically a 4x4 or 8x8 grid.
2. The grid consists of different types of cells:
 i. "S" (Start): The starting point for the agent.
ii. "F" (Frozen): Safe frozen surface, which the agent can walk on without any issue.
iii. "H" (Hole): Holes in the frozen surface. If the agent steps into a hole, it falls and fails.
iv. "G" (Goal): The goal location the agent needs to reach.
Agent:
1. The agent starts at the "S" cell and needs to navigate through the grid to reach the "G" cell.
2. The agent can take discrete actions such as moving UP, DOWN, LEFT, or RIGHT.
Objective:
1. The goal of the agent is to reach the "G" cell while avoiding the "H" cells. Success is defined 
as reaching the goal cell.
Challenges:
1. The ice on the frozen surface is slippery, so the agent doesn't always move in the intended 
direction. Instead, it moves in the chosen direction with a certain probability, often making it 
challenging to reach the goal.
2. The agent's objective is to learn a policy that maximizes the cumulative reward while 
navigating the grid.
For Example: The agent is on a grid of ice and must reach the goal while avoiding holes. The grid 
looks like this: Consider the following 4x4 grid:
in which agent starts at 1,
state 2 = F,
state 3 = F,
state 4 = F,
state 5 = F,
state 6 = H,
state 7 = F,
state 8 = H,
state 9 = F,
state 10 = F,
state 11 = F,
state 12 = H,
state 13 = H,
state 14 = F,
state 15 = F,
state 16 = G,

S: Start
F: Frozen surface (safe)
H: Hole (fall into the hole and lose)
G: Goal
Rewards are given as follows:
1. Reaching the goal ("G") cell: +1 (positive reward for success)
2. Falling into a hole ("H") cell: -1 (negative reward for failure)
3. All other actions: -0.1 (a small negative reward for taking actions, which encourages the 
agent to reach the goal with fewer steps)
Your task is to solve this problem using Markov Decision Process
please provide a neat and simple code using python """

import random

grid = [
    ["S", "F", "F", "F"],
    ["F", "H", "F", "H"],
    ["F", "F", "F", "H"],
    ["H", "F", "F", "G"],
]

rewards = {
    'S': 0,
    'F': -0.1,
    'H': -1,
    'G': 1
}

actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']

Policy = {
    (0, 0): 'RIGHT',
    (0, 1): 'DOWN',
    (0,2): 'DOWN',
    (0,3): 'DOWN',
    (1,0): 'RIGHT',
    (1,2): 'RIGHT',
    (2,0): 'UP',
    (2,3): 'RIGHT',
    (3,1): 'UP',
    (3,2): 'UP',
}

def policy_evaluation(grid, rewards, gamma=1.0, theta=0.0001, max_iterations=1000):
    V = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            V[(i, j)] = 0
    for i in range(max_iterations):
        delta = 0
        for state in V:
            if state in Policy:
                v = V[state]
                V[state] = 0
                for action in actions:
                    if Policy[state] == action:
                        prob = 0.8
                    else:
                        prob = 0.2 / 3
                    next_state = get_next_state(state, action)
                    reward = rewards[grid[next_state[0]][next_state[1]]]
                    V[state] += prob * (reward + gamma * V[next_state])
                delta = max(delta, abs(v - V[state]))
        if delta < theta:
            break
    return V

def get_next_state(state, action):
    if action == 'UP':
        next_state = (max(state[0] - 1, 0), state[1])
    elif action == 'DOWN':
        next_state = (min(state[0] + 1, len(grid) - 1), state[1])
    elif action == 'LEFT':
        next_state = (state[0], max(state[1] - 1, 0))
    elif action == 'RIGHT':
        next_state = (state[0], min(state[1] + 1, len(grid[0]) - 1))
    return next_state

def policy_improvement(grid, rewards, gamma=1.0):
    V = policy_evaluation(grid, rewards, gamma)
    policy = {}
    for state in V:
        if state in Policy:
            max_value = float('-inf')
            for action in actions:
                if Policy[state] == action:
                    prob = 0.8
                else:
                    prob = 0.2 / 3
                next_state = get_next_state(state, action)
                reward = rewards[grid[next_state[0]][next_state[1]]]
                value = prob * (reward + gamma * V[next_state])
                if value > max_value:
                    max_value = value
                    policy[state] = action
    return policy

def policy_iteration(grid, rewards, gamma=1.0, theta=0.0001, max_iterations=1000):
    policy = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            policy[(i, j)] = random.choice(actions)
    for i in range(max_iterations):
        old_policy = policy.copy()
        V = policy_evaluation(grid, rewards, gamma, theta, max_iterations)
        policy = policy_improvement(grid, rewards, gamma)
        if old_policy == policy:
            break
    return V, policy

V, policy = policy_iteration(grid, rewards)
print("Final Policy:")
for i in range(len(grid)):
    print([policy[(i, j)] if (i, j) in policy else ' ' for j in range(len(grid[0]))])
print("Final State Values:")
for i in range(len(grid)):
    print(["{0:.2f}".format(V[(i, j)]) if (i, j) in V else ' ' for j in range(len(grid[0]))])

# Reference: https://www.learndatasci.com/tutorials/reinforcement-q-learning-scratch-python-openai-gym/