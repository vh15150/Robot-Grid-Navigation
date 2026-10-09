# Multi-Robot Warehouse Planner - CSP Layer
# Uses Backtracking and AC-3 constraint propagation


def is_valid(robot, task, current_load):
    """Check robot capacity and permitted zone."""

    if current_load + task["load"] > robot["capacity"]:
        return False

    if task["zone"] not in robot["zones"]:
        return False

    return True


def assign_tasks(robots, tasks):
    """Assign tasks using backtracking."""

    assignments = {robot["id"]: [] for robot in robots}
    loads = {robot["id"]: 0 for robot in robots}

    # Assign more restrictive tasks first
    tasks = sorted(
        tasks,
        key=lambda task: sum(
            task["zone"] in robot["zones"]
            and task["load"] <= robot["capacity"]
            for robot in robots
        )
    )

    def backtrack(index):
        if index == len(tasks):
            return True

        task = tasks[index]

        for robot in robots:
            robot_id = robot["id"]

            if not is_valid(robot, task, loads[robot_id]):
                continue

            # Assign task
            assignments[robot_id].append(task)
            loads[robot_id] += task["load"]

            if backtrack(index + 1):
                return True

            # Backtrack if this assignment fails
            assignments[robot_id].pop()
            loads[robot_id] -= task["load"]

        return False

    if backtrack(0):
        return assignments

    return None
def ac3(robots, tasks):
    """Filter robots that cannot perform each task."""

    domains = {}

    for task in tasks:
        domains[task["id"]] = []

        for robot in robots:
            if (
                task["load"] <= robot["capacity"]
                and task["zone"] in robot["zones"]
            ):
                domains[task["id"]].append(robot["id"])

    print("\nAC-3: TASK DOMAINS")
    print("-" * 30)

    for task_id, possible_robots in domains.items():
        print(f"{task_id}: {possible_robots}")

    if any(not domain for domain in domains.values()):
        print("No suitable robot available for a task.")
        return None

    return domains

if __name__ == "__main__":

  if __name__ == "__main__":

    robots = [
        {"id": "R1", "capacity": 5, "zones": ["A", "B"]},
        {"id": "R2", "capacity": 3, "zones": ["B", "C"]},
        {"id": "R3", "capacity": 4, "zones": ["A", "C"]}
    ]

    tasks = [
        {"id": "T1", "load": 2, "zone": "A"},
        {"id": "T2", "load": 3, "zone": "B"},
        {"id": "T3", "load": 2, "zone": "C"},
        {"id": "T4", "load": 4, "zone": "A"}
    ]

    domains = ac3(robots, tasks)

    if domains is not None:
        result = assign_tasks(robots, tasks)
    else:
        result = None

    print("\nMULTI-ROBOT TASK ASSIGNMENT")
    print("-" * 30)

    if result is None:
        print("No valid assignment found.")
    else:
        for robot_id, assigned_tasks in result.items():
            task_ids = [task["id"] for task in assigned_tasks]
            print(f"{robot_id}: {task_ids}")