Ǫuestion 2: Optimisation - Telecommunication Tower Placement [25 Marks]
Background
MTC is expanding its 5G network across a designated 10 × 10 regional grid. To minimise signal interference and navigate physical obstacles, MTC needs to place 8 signal boosters in accordance with strict spatial and environmental guidelines. This is a Constraint Satisfaction Problem (CSP) that extends the logic of the classic N-Queens puzzle into infrastructure planning.
Problem Formulation
•
Variables: The 8 towers to be placed (𝑇1,𝑇2,…,𝑇8).
•
Domain: All 100 cells in the 10 × 10 grid, represented as (row, col) coordinates where 0≤ 𝑟𝑜𝑤,𝑐𝑜𝑙≤ 9.
•
Initial State: An empty assignment where no towers have been placed.
•
Goal State: A complete assignment where all 8 towers are placed without violating any constraints.
Constraints
Your solver must ensure that the following conditions are met for any two towers 𝑇𝑖 and 𝑇𝑗:
•
Horizontal/Vertical (Signal Overlap): No two towers can share the same row or column.
•
Proximity (Interference Buffer): No two towers can be placed in adjacent cells, including all diagonal neighbours.
•
Terrain (Prohibited Zones): Towers cannot be placed on "Mountain" cells, which represent physical terrain obstructions defined in the input lists below.
Specification
Implement a Telecom_CSP_Solver class that includes the following logic based on the lecture methodologies:
•
backtrack(assignment): The core recursive function that attempts to build a valid assignment of towers to cells.
•
Minimum Remaining Values (MRV): A heuristic to select the next tower based on which one has the fewest remaining valid cells in its domain.
•
Forward Checking: After each tower is placed, prune the domains of all unassigned towers to remove cells that would now violate constraints.
•
is_consistent(assignment, cell): A helper function to verify if a specific placement satisfies all active constraints.
Using matplotlib, generate a plot of the final 10 × 10 grid:
•
Towers: Mark MTC booster locations clearly (e.g., Blue 'T').
•
Mountain Cells: Shaded differently (e.g., Brown 'M') to indicate avoided areas.
•
Grid Layout: Clearly visible to verify adherence to row/column and proximity rules.
Test Scenarios
Level 1: Coastal Region (Easy)
•
Mountains: [(0,0), (1,1), (9,9)]
•
Objective: Establish basic row, column, and diagonal proximity logic.
Level 2: Highlands Region (Medium)
•
Mountains: [(2,2), (2,3), (3,2), (3,3), (7,8), (8,7), (8,8)]
•
Objective: Successfully navigate around clusters of prohibited terrain.
Level 3: Brandberg Region (Hard)
•
Mountains: [(0,5), (1,5), (2,5), (3,5), (4,5), (5,0), (5,1), (5,2), (5,3), (5,4)]
•
Objective: Solve the grid where mountains form a partial "wall," forcing towers into high-constraint clusters.