from collections import deque
from time import perf_counter


def bfs(grid, start, goal):
    """Find the shortest path using BFS."""

    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        position, path = queue.popleft()

        if position == goal:
            return path

        row, col = position

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        for dr, dc in directions:
            nr = row + dr
            nc = col + dc
            next_position = (nr, nc)

            if (
                0 <= nr < len(grid)
                and 0 <= nc < len(grid[0])
                and grid[nr][nc] == 0
                and next_position not in visited
            ):
                visited.add(next_position)
                queue.append((next_position, path + [next_position]))

    return None


def main():
    print("=" * 45)
    print(" SINGLE VS MULTI-ROBOT COMPARISON")
    print("=" * 45)

    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]

    # Two tasks to complete.
    tasks = [
        ((0, 0), (0, 4)),
        ((4, 0), (4, 4))
    ]

    print("\nWarehouse grid: 5 x 5")
    print("Tasks to complete:", len(tasks))

    # One robot completes both tasks sequentially.
    single_total_steps = 0
    single_paths = []

    for start, goal in tasks:
        path = bfs(grid, start, goal)

        if path is None:
            print("Single robot cannot reach a task.")
            return

        single_paths.append(path)
        single_total_steps += len(path) - 1

    # Two robots complete one task each.
    multi_total_steps = 0
    multi_paths = []

    for start, goal in tasks:
        path = bfs(grid, start, goal)

        if path is None:
            print("A robot cannot reach its task.")
            return

        multi_paths.append(path)
        multi_total_steps = max(
            multi_total_steps,
            len(path) - 1
        )

    print("\n--- Single-Robot Plan ---")

    for index, path in enumerate(single_paths, start=1):
        print(f"Task {index}: {path}")

    print("Total movement steps:", single_total_steps)

    print("\n--- Multi-Robot Plan ---")

    for index, path in enumerate(multi_paths, start=1):
        print(f"Robot {index}: {path}")

    print("Warehouse completion time:", multi_total_steps)

    if single_total_steps > 0:
        improvement = (
            (single_total_steps - multi_total_steps)
            / single_total_steps
        ) * 100

        print(f"\nEstimated completion-time reduction: {improvement:.1f}%")

print("\n--- Explained Plan ---")
print("1. Robot 1 starts at (0, 0) and moves to (0, 4).")
print("2. Robot 2 starts at (4, 0) and moves to (4, 4).")
print("3. Each robot moves one cell per time step.")
print("4. The robots use separate rows, avoiding collisions.")
print("5. Each route requires 4 movement steps.")
print("6. Both robots finish at time step 4.")
print("7. One robot would require 8 movement steps")
print("   to complete both tasks sequentially.")
print("8. Two robots reduce completion time by 50%")
print("   in this example.")

if __name__ == "__main__":
    main()