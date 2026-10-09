# Multi-Robot Warehouse Planner Using Artificial Intelligence

## 1. Project Title

Multi-Robot Warehouse Planner Using Artificial Intelligence

## 2. Introduction

This project extends Robot Grid Navigation into a Multi-Robot
Warehouse Planner. It demonstrates how Artificial Intelligence
can help robots navigate grids, avoid obstacles, assign tasks,
and schedule movements.

## 3. Objectives

1. Find shortest paths while avoiding obstacles.
2. Assign tasks to multiple robots.
3. Schedule robot movements while checking for collisions.
4. Demonstrate Move, Pick, Drop, and Charge actions.
5. Compare single-robot and multi-robot completion times.
6. Analyse movement uncertainty using expected costs.

## 4. Technologies Used

- Python
- Breadth-First Search (BFS)
- Constraint Satisfaction Problems (CSP)
- Backtracking
- AC-3 constraint propagation
- STRIPS-style planning actions
- Pytest

## 5. Grid Representation

0 = Free space
1 = Obstacle
S = Starting position
G = Goal position
# = Obstacle
* = Selected path
. = Free cell

The BFS demonstration uses a 5 x 5 grid.

## 6. Project Modules

### 6.1 BFS Pathfinding

File: src/app.py

BFS explores the grid level by level. When each movement has
the same cost, BFS finds a shortest path if one exists.

### 6.2 CSP Task Assignment

File: src/csp.py

The module assigns tasks to robots using backtracking.
The example considers robot capacity and zone restrictions.
AC-3 constraint propagation requires further validation.

### 6.3 STRIPS-Style Actions

File: src/strips.py

The robot demonstrates Move, Pick, Drop, and Charge actions.
It also checks a safety restriction for a forbidden cell.

### 6.4 Responsible AI

File: src/responsible_ai.py

The module models movement success with a probability of 0.8
and compares expected costs for alternative routes.

Expected attempts for n successful movements:

Expected attempts = n / 0.8

This is an estimate under the model's assumptions.

### 6.5 Multi-Robot Scheduling

File: src/multi_robot.py

The module schedules multiple robots over time. It checks
same-cell conflicts and opposite-direction swaps. Waiting is
allowed, and completed robots remain at their goals.

### 6.6 Performance Comparison

File: src/comparison.py

The module compares a sequential single-robot plan with a
multi-robot plan for independent tasks.

## 7. Testing

The BFS module contains 10 automated tests using pytest.

The tests cover shortest paths, start and goal conditions,
obstacles, unreachable goals, expanded nodes, single-cell
grids, and longer paths.

Recorded test result: 10 tests passed.

The other modules have been tested with example inputs.
Additional automated tests are needed for their edge cases.

## 8. Results

### BFS Result

The tested 5 x 5 grid produced a path containing 8 movements
and expanded 19 nodes.

### Multi-Robot Result

Two robots successfully completed the tested routes without
same-cell conflicts or opposite-direction swaps.

### Performance Comparison

Single-robot completion time: 8 time steps
Two-robot completion time: 4 time steps

Completion-time reduction:

((8 - 4) / 8) x 100 = 50%

This result applies to the tested example only.

## 9. Limitations and Future Improvements

1. Validate AC-3 constraint propagation.
2. Add deadline-aware task scheduling.
3. Improve scheduling for complex warehouse layouts.
4. Add automated tests for all modules.
5. Integrate task assignment and scheduling.
6. Add visualisations of robot routes.

## 10. Conclusion

The project demonstrates several Artificial Intelligence
concepts through Python modules. BFS finds paths around
obstacles, backtracking assigns tasks, STRIPS-style actions
demonstrate robot behaviour, and the multi-robot planner
schedules movements while checking for collisions.

In the tested example, two robots reduced completion time
from 8 steps to 4 steps, giving a 50% reduction.
Further validation and integration are needed to confirm
all project requirements.