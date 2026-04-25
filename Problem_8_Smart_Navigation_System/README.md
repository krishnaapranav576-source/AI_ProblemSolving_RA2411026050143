# Problem 8 – Smart Navigation System (BFS, DFS)

## Problem Description

A navigation system is required to find routes between different locations similar to Google Maps.

The user gives:

* Start node
* Goal node
* Graph connections

The system dynamically creates the graph and finds the path between the start and goal nodes.

## Algorithms Used

* Breadth First Search (BFS)
* Depth First Search (DFS)

## Features

* Finds path from start node to goal node
* Compares BFS and DFS
* Shows visited nodes
* Interactive web interface using Flask

## Execution Steps

1. Install Python
2. Install Flask using:

pip install flask

3. Run the program using:

python app.py

4. Open browser and go to:

http://127.0.0.1:5000

5. Enter Start Node and Goal Node

6. Click Find Path

7. View BFS and DFS results

## Sample Input

Start Node: A

Goal Node: F

## Sample Output

### BFS Result

Path:
A → C → F

Visited Nodes:
A, B, C, D, E, F

### DFS Result

Path:
A → B → E → F

Visited Nodes:
A, B, D, E, F

## Conclusion

BFS gives the shortest path while DFS may not always give the shortest path.
