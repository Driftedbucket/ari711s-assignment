import numpy as np
from collections import defaultdict

class GridworldSARSA:
    
    def __init__(self, grid_size=5, gamma=0.9, epsilon=0.1, alpha=0.2):
        self.grid_size=grid_size
        self.gamma=gamma
        self.epsilon=epsilon
        self.alpha=alpha
