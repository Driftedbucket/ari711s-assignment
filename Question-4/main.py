import numpy as np
from collections import defaultdict

class GridworldSARSA:
    
    def __init__(self, grid_size=5, gamma=0.9, epsilon=0.1, alpha=0.2):
        self.grid_size=grid_size
        self.gamma=gamma
        self.epsilon=epsilon
        self.alpha=alpha

        #speical states and theior rewards stored in a tuple   
        self.special_states={"A":(0,1),
                             "B":(0,3)}
        self.next_to_states={"A":(4,1),
                             "B":(2,3)}
        self.special_rewards={"A":10,
                              "B":5}
        #possible actions
        self.actions={"north","south","east","west"}

def _print_initialization(self):
        
        print("Initializing Gridworld...")
        print(f"Grid size: {self.grid_size}x{self.grid_size}")
        print(f"Special_states = {self.special_states}")
        print(f"Next_to_states = {self.next_to_states}")
        print(f"Special_rewards = {self.special_rewards}")
        print()
        print("Starting Q-learning with parameters:")
        print(f"γ = {self.gamma}")
        print(f"ε = {self.epsilon}")
        print(f"α = {self.alpha}")

def _is_special_state(self, state):
        """Check if state is a special state and return its name"""
        for name, pos in self.special_states.items():
            if state == pos:
                return name
        return None

def _get_next_state_and_reward(self, state, action):
        
        row, col = state
        
        # Check if current state is special
        special_name = self._is_special_state(state)
        if special_name:
            # From special state, any action transitions to next_to_state with special reward
            reward = self.special_rewards[special_name]
            next_state = self.next_to_states[special_name]
            return next_state, reward
        
        # Normal state transitions
        if action == 0:  # north
            new_row, new_col = row - 1, col
        elif action == 1:  # south
            new_row, new_col = row + 1, col
        elif action == 2:  # east
            new_row, new_col = row, col + 1
        elif action == 3:  # west
            new_row, new_col = row, col - 1
        
        # Check if new position is within grid
        if 0 <= new_row < self.grid_size and 0 <= new_col < self.grid_size:
            next_state = (new_row, new_col)
            reward = 0
        else:
            # Moving off grid keeps agent in same state with penalty
            next_state = state
            reward = -1
        
        return next_state, reward
