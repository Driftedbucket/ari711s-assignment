Question 1: Search Algorithms - The Warehouse Logistics Bot [25 Marks]

Background

In Practical Lab 1, we implemented the two uninformed search algorithms, DFS and BFS, to navigate a basic maze. For this task, you are tasked with upgrading the navigation system for an automated warehouse robot (AGV) operating in a logistics centre in Windhoek. Unlike a simple maze, this environment features high-density shelving units and designated charging zones.

Task

You must write a Python program that finds the most efficient path from the Charging Station (A) to a specific Product Bin (B). You will implement and compare two informed search algorithms: Greedy Best-First Search and A* Search.

Problem Formulation

The maze is represented as a text file, which you need to parse and model as a grid- world environment by implementing two algorithms to find the shortest path from A to
B. This problem can be framed as a search problem where:

•States: Grid coordinates (row, col) representing the robot's position in the warehouse.
•Actions: Movements to adjacent, non-shelf cells: forward, down, left, right
•Initial State: The position marked A.
•Goal State: The position marked B.
•Heuristic: Use the Euclidean Distance between the current node (𝑥1,𝑦1) and the goal (𝑥2,𝑦2):ℎ(𝑛)=√(𝑥1−𝑥2)2+(𝑦1−𝑦2)2

Your program must include the following:

1.
Warehouse Class: This class must:

•Read and parse the warehouse layout from a .txt file.
•Locate the coordinates for A and B.
•Store the locations of shelving units (walls).
•Implement a neighbors(state) function returning valid adjacent aisles.

2.
solve(algorithm="greedy" or "astar") Method:

•Utilise a Priority Queue frontier.
•For Greedy: Priority is determined solely by ℎ(𝑛).
•For A*: Priority is determined by 𝑓(𝑛) = 𝑔(𝑛) + ℎ(𝑛).
•Track and store all explored states to prevent cycles.

3.
Node Class: Store the state, parent node, action taken, and path cost (𝑔(𝑛)).

4.
Visual Output: Export an image named warehouse_path.png. The image must use distinct colours to show:
oThe robot's optimal path.
oShelving units (Walls).
oStates that were explored but are not part of the final path.

Note: Download the warehouse.txt files here to test your program.(They've been included in the folder already)