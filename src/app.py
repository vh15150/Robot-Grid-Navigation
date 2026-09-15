from collections import deque


# 0 = free space
# 1 = obstacle
GRID = [
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

START = (0, 0)
GOAL = (4, 4)


def bfs(grid, start, goal):
    """Find the shortest path using Breadth-First Search."""

    rows = len(grid)
    cols = len(grid[0])

    queue = deque([start])
    visited = {start}
    parent = {start: None}

    # Up, Down, Left, Right
    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    while queue:
        current = queue.popleft()

        if current == goal:
            break

        row, col = current

        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc
            next_cell = (new_row, new_col)

            # Check whether the new cell is inside the grid
            if not (0 <= new_row < rows and 0 <= new_col < cols):
                continue

            # Check whether it is an obstacle
            if grid[new_row][new_col] == 1:
                continue

            # Check whether it was already visited
            if next_cell in visited:
                continue

            visited.add(next_cell)
            parent[next_cell] = current
            queue.append(next_cell)

    # No path found
    if goal not in parent:
        return None, len(visited)

    # Reconstruct the path
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    return path, len(visited)


def display_grid(grid, path, start, goal):
    """Display the grid and highlight the discovered path."""

    path_set = set(path) if path else set()

    for row in range(len(grid)):
        line = []

        for col in range(len(grid[0])):
            position = (row, col)

            if position == start:
                line.append("S")
            elif position == goal:
                line.append("G")
            elif grid[row][col] == 1:
                line.append("#")
            elif position in path_set:
                line.append("*")
            else:
                line.append(".")

        print(" ".join(line))


def main():
    print("ROBOT GRID NAVIGATION")
    print("=" * 30)

    path, nodes_expanded = bfs(GRID, START, GOAL)

    print("\nGrid and discovered path:")
    display_grid(GRID, path, START, GOAL)

    if path:
        print("\nPath found!")
        print("Path:", path)
        print("Number of moves:", len(path) - 1)
        print("Nodes expanded:", nodes_expanded)
    else:
        print("\nNo path found.")


if __name__ == "__main__":
    main()