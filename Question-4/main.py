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
