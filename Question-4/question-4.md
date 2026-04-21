Python program that implements the SARSA algorithm for a Gridworld Markov Decision Process (MDP).

### Environment Description:
- Grid size: 5x5
- States: Each cell represents a state (row, col)
- Actions: ['north', 'south', 'east', 'west']
- Actions are deterministic:
  - Moving off the grid keeps the agent in the same state and gives reward = -1
  - All normal transitions give reward = 0

### Special States:
- A = (0,1): 
    - Any action from A gives reward +10 and moves agent to A' = (4,1)
- B = (0,3):
    - Any action from B gives reward +5 and moves agent to B' = (2,3)

### Parameters:
- Discount factor γ = 0.9
- Learning rate α = 0.2
- Exploration rate ε = 0.1 (epsilon-greedy policy)
- Episodes = 5000
- Steps per episode = 5000

---

### Tasks:

1. **Initialize the environment**
   - Represent grid states
   - Define transition function
   - Define reward function

2. **Implement SARSA (on-policy TD control):**
   Use the update rule:
   Q(s,a) ← Q(s,a) + α [r + γ Q(s',a') − Q(s,a)]

3. **Use ε-greedy policy for action selection**

4. **Train the agent**
   - Loop through episodes
   - Update Q-values using SARSA

5. **After training:**
   - Compute the optimal value function V(s) = max_a Q(s,a)
   - Derive optimal policy π(s) = argmax_a Q(s,a)

---

### Output Requirements:

Print the following:

1. Initialization info:

Initializing Gridworld...
Grid size: 5x5
Special_states = {'A': (0,1), 'B': (0,3)}
Next_to_states = {'A': (4,1), 'B': (2,3)}
Special_rewards = {'A': 10, 'B': 5}

Starting Q-learning with parameters:
γ = 0.9
ε = 0.1
α = 0.2
Episodes = 5000
Steps = 5000


2. Final Value Function (5x5 grid, formatted to 2 decimal places)

3. Optimal Policy (text form):
Example:

east north west north west
north north west west west
...


4. Optimal Policy (arrow form):
Use:
- ↑ for north
- ↓ for south
- → for east
- ← for west

---

### Additional Requirements:
- Use clean modular code:
  - functions for environment, action selection, SARSA update
- Use NumPy for arrays
- Ensure reproducibility (set random seed)
- Format outputs neatly (grid layout)

---

### Goal:
The resulting value function and policy should closely match the known optimal solution for t