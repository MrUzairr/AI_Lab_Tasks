import numpy as np
import random


class FrozenMDP:
    def __init__(self, nc, nr):
        self.nc = nc
        self.nr = nr
        
    def states(self):
        return np.arange(1, self.nc * self.nr + 1)

    def get_block_no(self, s):
        return (s - 1) // self.nc + 1, (s - 1) % self.nc + 1

    def get_state_no(self, x, y):
        return (x - 1) * self.nc + y

    def Start(self):
        return 1

    def Goal(self):
        return self.nc * self.nr

    def actions(self, s):
        action = []
        x, y = self.get_block_no(s)
        if y - 1 >= 1:
            action.append('Left')
        if y + 1 <= self.nc:
            action.append('Right')
        if x - 1 >= 1:
            action.append('Up')
        if x <= self.nr:
            action.append('Down')

        return action

    def FailureStates(self):
        return [6, 8, 12, 13]

    def SuccessState(self):
        return [16]

    def isGoal(self, s):
        if s in self.FailureStates():
            return True
        if s in self.SuccessState():
            return True
        return False

    def reward(self, state, action, new_state):
        if new_state in self.states():
            if new_state in self.FailureStates():
                return -1
            elif self.isGoal(new_state):
                return 1

            return -0.1
        return 0

    def transition_probability(self, s, a, new_state):
        x, y = self.get_block_no(s)

        if a == "Left":
            y -= 1
        elif a == "Right":
            y += 1
        elif a == "Up":
            x -= 1
        elif a == "Down":
            x += 1

        s_calc = self.get_state_no(x, y)

        if s_calc == new_state:
            return 0.6
        elif new_state in self.FailureStates():
            return 0.4
        else:
            return 0.0

    def transition(self, s, a):
        x, y = self.get_block_no(s)

        if a == "Left":
            y -= 1
        elif a == "Right":
            y += 1
        elif a == "Up":
            x -= 1
        elif a == "Down":
            x += 1

        s_calc = self.get_state_no(x, y)
        return s_calc

    def transitions(self, s):
        transition_states = []
        actions = self.actions(s)
        for action in actions:
            transition_states.append(self.transition(s, action))

        return transition_states


def minimum_reward_to_goal(mdp, state, total_reward, visited, parent_map):
    
    if mdp.isGoal(state):
        path = [state]
        current_state = state
        while current_state != mdp.Start():
            if parent_map[current_state] <= (mdp.nc * mdp.nr):
                path.insert(0, parent_map[current_state])
            current_state = parent_map[current_state]
        return total_reward, state, path,  'Failure' if state in mdp.FailureStates() else 'Goal'


    visited.add(state)

    min_reward = None
    best_path = None

    for action in mdp.actions(state):
        next_state = mdp.transition(state, action)
        reward = mdp.reward(state, action, next_state)
        print("Reward",reward,"State",state)

        if next_state not in visited and next_state not in mdp.FailureStates():
            parent_map[next_state] = state

            sub_reward, sub_goal, sub_path, sub_status = minimum_reward_to_goal(
                mdp, next_state, total_reward + reward, visited, parent_map)

            if sub_reward is not None and (min_reward is None or sub_reward < min_reward):
                min_reward = sub_reward
                best_path = sub_path

    return min_reward, '16', best_path, 'Goal'


a = FrozenMDP(4, 4)
print("Initial State:", a.Start())
print("Reward: ", minimum_reward_to_goal(a, a.Start(), 0, set(), {}))
