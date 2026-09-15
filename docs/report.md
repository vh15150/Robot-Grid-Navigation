# Robot Grid Navigation

## 1. Project Title
Robot Grid Navigation using Breadth-First Search (BFS)

## 2. Objective
The objective of this project is to find the shortest path for a robot
from a starting position to a goal position in a grid while avoiding obstacles.

## 3. Algorithm Used
Breadth-First Search (BFS) is used to find the shortest path.

BFS explores the grid level by level. Since every movement has the same cost,
the first time the goal is reached, the path found is the shortest path.

## 4. Grid Representation

0 = Free space  
1 = Obstacle

The project uses a 5 × 5 grid.

## 5. Symbols

S = Start position  
G = Goal position  
# = Obstacle  
* = Shortest path  
. = Free space

## 6. Program Structure

- `src/app.py` - Main BFS implementation
- `tests/test_app.py` - Automated test cases
- `docs/report.md` - Project report
- `README.md` - Project information

## 7. Testing

The project contains 10 automated test cases using pytest.

The tests check:

1. Shortest path
2. Start equals goal
3. No available path
4. Obstacle avoidance
5. Path starts at start position
6. Path ends at goal position
7. Path does not use obstacles
8. Nodes expanded
9. Single-cell grid
10. Longer path

## 8. Result

All 10 test cases passed successfully.

## 9. Conclusion

The Robot Grid Navigation project successfully demonstrates the use of
Breadth-First Search to find the shortest path in a grid containing obstacles.
The program also includes automated testing using pytest.