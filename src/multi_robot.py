from collections import deque


def get_grid():
    """Get a valid grid from the user."""
    while True:
        try:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))

            if rows <= 0 or cols <= 0:
                print("Rows and columns must be positive.")
                continue

            break
        except ValueError:
            print("Enter valid whole numbers.")

    grid = []

    print("\nEnter grid values:")
    print("0 = Free cell, 1 = Obstacle")

    for r in range(rows):
        while True:
            values = input(
                f"Enter row {r + 1} ({cols} values separated by spaces): "
            ).split()

            if len(values) != cols:
                print(f"Enter exactly {cols} values.")
                continue

            if any(value not in ("0", "1") for value in values):
                print("Only 0 and 1 are allowed.")
                continue

            grid.append([int(value) for value in values])
            break

    return grid


def get_position(name, grid):
    """Get a valid free-cell position."""
    rows = len(grid)
    cols = len(grid[0])

    while True:
        try:
            values = input(
                f"Enter {name} row and column (example: 0 0): "
            ).split()

            if len(values) != 2:
                print("Enter two numbers separated by a space.")
                continue

            r, c = map(int, values)

            if not (0 <= r < rows and 0 <= c < cols):
                print("Position is outside the grid.")
                continue

            if grid[r][c] == 1:
                print("That cell contains an obstacle.")
                continue

            return (r, c)

        except ValueError:
            print("Enter valid whole numbers.")


def get_neighbors(grid, position):
    """Return free neighboring cells."""
    r, c = position
    rows = len(grid)
    cols = len(grid[0])

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    neighbors = []

    for dr, dc in directions:
        nr = r + dr
        nc = c + dc

        if (
            0 <= nr < rows
            and 0 <= nc < cols
            and grid[nr][nc] == 0
        ):
            neighbors.append((nr, nc))

    return neighbors


def plan_robot(
    grid,
    start,
    goal,
    reserved_cells,
    reserved_edges,
    max_time
):
    """
    Find a safe path using time-based BFS.

    A robot can move to a neighboring cell or wait.
    Reserved cells prevent same-cell collisions.
    Reserved edges prevent opposite-direction swaps.
    """

    if start in reserved_cells.get(0, set()):
        return None

    start_state = (start, 0)
    queue = deque([start_state])

    previous = {start_state: None}
    goal_state = None

    while queue:
        position, time = queue.popleft()

        if position == goal:
            goal_state = (position, time)
            break

        if time >= max_time:
            continue

        next_time = time + 1

        # Moving to a neighbor or waiting in the current cell.
        possible_positions = get_neighbors(grid, position)
        possible_positions.append(position)

        for next_position in possible_positions:

            # Prevent two robots from occupying the same cell.
            if next_position in reserved_cells.get(next_time, set()):
                continue

            # Prevent robots from swapping positions.
            reverse_edge = (next_position, position)

            if reverse_edge in reserved_edges.get(next_time, set()):
                continue

            next_state = (next_position, next_time)

            if next_state in previous:
                continue

            previous[next_state] = (position, time)
            queue.append(next_state)

    if goal_state is None:
        return None

    # Reconstruct the path.
    path = []
    state = goal_state

    while state is not None:
        position, time = state
        path.append(position)
        state = previous[state]

    path.reverse()
    return path


def plan_multiple_robots(grid, robots):
    """Plan collision-free schedules for multiple robots."""

    rows = len(grid)
    cols = len(grid[0])

    # Search horizon for time-based BFS.
    max_time = rows * cols * max(1, len(robots)) * 4 + 30

    reserved_cells = {}
    reserved_edges = {}
    schedules = {}

    # Plan robots in their input order.
    for robot_id, start, goal in robots:

        path = plan_robot(
            grid,
            start,
            goal,
            reserved_cells,
            reserved_edges,
            max_time
        )

        if path is None:
            print(
                f"\nRobot {robot_id}: No safe schedule found."
            )
            continue

        schedules[robot_id] = path

        # Reserve every cell occupied along the route.
        for time, position in enumerate(path):
            reserved_cells.setdefault(time, set()).add(position)

        # Reserve movement edges to prevent opposite-direction swaps.
        for time in range(1, len(path)):
            previous_position = path[time - 1]
            current_position = path[time]

            reserved_edges.setdefault(time, set()).add(
                (previous_position, current_position)
            )

        # A robot remains at its goal after it finishes.
        goal_time = len(path) - 1

        for time in range(goal_time + 1, max_time + 1):
            reserved_cells.setdefault(time, set()).add(goal)

    return schedules


def display_schedules(schedules):
    """Display each robot's movement schedule."""

    print("\n" + "=" * 45)
    print(" ROBOT MOVEMENT SCHEDULES")
    print("=" * 45)

    if not schedules:
        print("No safe schedules were found.")
        return

    for robot_id, path in schedules.items():
        print(f"\nRobot {robot_id}:")
        print("Time | Position")
        print("-" * 25)

        for time, position in enumerate(path):
            print(f"{time:5} | {position}")

        print(f"Total time steps: {len(path) - 1}")

    completion_time = max(
        len(path) - 1 for path in schedules.values()
    )

    print("\nWarehouse completion time:", completion_time)
    print(f"Successful schedules: {len(schedules)}")

    print("\nCollision avoidance:")
    print("- Same-cell collisions are checked.")
    print("- Opposite-direction swaps are checked.")
    print("- Waiting is allowed.")
    print("- Completed robots remain at their goals.")


def main():
    print("=" * 45)
    print(" MULTI-ROBOT WAREHOUSE PLANNER")
    print(" TIME-BASED COLLISION AVOIDANCE")
    print("=" * 45)

    grid = get_grid()

    while True:
        try:
            number_of_robots = int(
                input("\nEnter number of robots: ")
            )

            if number_of_robots <= 0:
                print("Enter at least one robot.")
                continue

            break

        except ValueError:
            print("Enter a valid whole number.")

    robots = []
    used_starts = set()

    for robot_number in range(1, number_of_robots + 1):
        print(f"\n--- Robot {robot_number} ---")

        while True:
            start = get_position("start", grid)

            if start in used_starts:
                print("Another robot already uses this start.")
                continue

            break

        goal = get_position("goal", grid)

        used_starts.add(start)
        robots.append((robot_number, start, goal))

    schedules = plan_multiple_robots(grid, robots)
    display_schedules(schedules)


if __name__ == "__main__":
    main()