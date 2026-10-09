# Multi-Robot Warehouse Planner Using Artificial Intelligence

## 1. Project Title

Multi-Robot Warehouse Planner Using Artificial Intelligence

## 2. Introduction

Robot navigation is an important application of Artificial Intelligence. Robots in a warehouse need to find paths, avoid obstacles, complete tasks, and prevent collisions.

This project extends basic Robot Grid Navigation into a Multi-Robot Warehouse Planner. It demonstrates pathfinding, task assignment, planning actions, collision avoidance, and movement-cost analysis.

## 3. Objectives

The main objectives are:

- Find the shortest path from a starting position to a goal.
- Avoid obstacles during navigation.
- Assign tasks to multiple robots.
- Schedule robot movements while checking for collisions.
- Demonstrate planning actions such as Move, Pick, Drop, and Charge.
- Compare single-robot and multi-robot completion times.
- Analyse movement uncertainty using expected costs.

## 4. Technologies Used

- Python
- Breadth-First Search (BFS)
- Constraint Satisfaction Problems (CSP)
- Backtracking
- AC-3 constraint propagation
- STRIPS-style planning actions
- Pytest

**Note:** The implementation and testing of each listed technique must be verified before claiming full compliance.

## 5. Grid Representation

The warehouse is represented as a grid.

| Symbol | Meaning |
|---|---|
| 0 | Free cell |
| 1 | Obstacle |
| S | Starting position |
| G | Goal position |
| * | Selected path |
| . | Free cell |

The BFS demonstration uses a 5 × 5 grid.

## 6. Project Modules

### 6.1 BFS Pathfinding

**File:** `src/app.py`

Breadth-First Search explores the grid level by level. When every movement has the same cost, BFS finds a shortest path if a path exists.

Run:

```bash
python -m src.app
```

### 6.2 CSP Task Assignment

**File:** `src/csp.py`

The task-assignment module assigns tasks to robots using backtracking. The example considers robot capacity and zone restrictions.

The module also displays task domains associated with its AC-3 processing. Constraint propagation should be validated separately before claiming a complete AC-3 implementation.

Run:

```bash
python -m src.csp
```

### 6.3 STRIPS-Style Planning Actions

**File:** `src/strips.py`

The robot demonstrates four actions:

- **Move:** Move to another permitted cell.
- **Pick:** Pick up a product.
- **Drop:** Deliver a product.
- **Charge:** Restore the battery.

The module also demonstrates a safety restriction for a cell where a human is nearby.

Run:

```bash
python -m src.strips
```

### 6.4 Responsible AI and Movement Uncertainty

**File:** `src/responsible_ai.py`

The module models movement success with a probability of 0.8 and compares expected movement costs for alternative routes.

For a route requiring `n` successful movements, the expected number of attempts under the independent-trial model is:

E[attempts] = n / 0.8

This is an estimate under the model's assumptions, not a guarantee of actual completion time.

Run:

```bash
python -m src.responsible_ai
```

### 6.5 Multi-Robot Scheduling

**File:** `src/multi_robot.py`

The module plans routes for multiple robots over time. It checks for same-cell conflicts and opposite-direction swaps, permits waiting, and keeps completed robots at their goals.

Run:

```bash
python -m src.multi_robot
```

Follow the terminal prompts to enter the grid, obstacles, robot starting positions, and goals.

### 6.6 Performance Comparison

**File:** `src/comparison.py`

The comparison module demonstrates how multiple robots can complete independent tasks simultaneously and compares the completion time with a sequential single-robot plan.

Run:

```bash
python -m src.comparison
```

## 7. Installation and Setup

### Prerequisites

- Python 3
- Git
- Visual Studio Code or another Python editor

### Clone the repository

```bash
git clone https://github.com/vh15150/Robot-Grid-Navigation.git
cd Robot-Grid-Navigation
```

### Install dependencies

Install the project requirements:

```bash
python -m pip install -r requirements.txt
```

Install pytest if it is not included in the requirements:

```bash
python -m pip install pytest
```

### Run the tests

```bash
python -m pytest -v
```

## 8. Testing

The BFS module has 10 automated tests using pytest.

The tests cover:

1. Shortest path
2. Start equals goal
3. No available path
4. Obstacle avoidance
5. Correct starting position
6. Correct goal position
7. Path avoids obstacles
8. Nodes expanded
9. Single-cell grid
10. Longer path

**Recorded result:** All 10 BFS tests passed in the reported test run.

The other modules have also been run using example inputs. Additional automated tests are needed to validate their edge cases and constraints.

## 9. Results and Analysis

### 9.1 BFS Result

The tested 5 × 5 grid produced a path with 8 movements and 19 expanded nodes.

### 9.2 Multi-Robot Scheduling Result

In the tested scenarios, two robots received routes without same-cell conflicts or opposite-direction swaps.

These results demonstrate the tested examples and do not guarantee conflict-free scheduling for every possible warehouse layout.

### 9.3 Single-Robot vs. Multi-Robot Comparison

For the example containing two independent tasks:

| Measurement | Single Robot | Two Robots |
|---|---:|---:|
| Completion time | 8 time steps | 4 time steps |
| Tasks completed | 2 | 2 |

The estimated completion-time reduction is:

Completion-time reduction = ((8 - 4) / 8) × 100 = 50%

This result applies to the tested example. Other layouts and tasks may produce different results.

### 9.4 Responsible AI Result

The demonstration assumes a movement success probability of 80%.

For Route A with 5 successful movements:

Expected attempts = 5 / 0.8 = 6.25

For Route B with 6 successful movements:

Expected attempts = 6 / 0.8 = 7.5

The program selects Route A because it has the lower expected movement cost under the specified model.

## 10. Limitations and Future Improvements

The project can be improved by:

- Validating AC-3 constraint propagation with dedicated tests.
- Adding explicit deadline-aware task scheduling.
- Improving multi-robot scheduling for more complex warehouse layouts.
- Adding automated tests for CSP, STRIPS, and movement uncertainty.
- Integrating task assignment, planning, and scheduling into one workflow.
- Adding visualisations of robot routes and performance.
- Validating the roll-number-based random seed and assigned project variant.

## 11. Conclusion

The Multi-Robot Warehouse Planner demonstrates several Artificial Intelligence concepts through Python modules. BFS finds paths around obstacles, backtracking assigns tasks, STRIPS-style actions demonstrate robot behaviour, and the multi-robot planner schedules movements while checking for collisions.

The performance comparison shows a 50% reduction in completion time for the tested example when two robots complete independent tasks in parallel.

Further validation, integration, and testing are needed to confirm all project requirements.

## 12. Author and Repository

**Project:** Multi-Robot Warehouse Planner Using Artificial Intelligence

**GitHub repository:** https://github.com/vh15150/Robot-Grid-Navigation