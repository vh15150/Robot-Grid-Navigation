# Robot Grid Navigation - Responsible AI
# Uncertain Movement, Route Comparison and Explanation Log

import random

# Movement success probability
SUCCESS_PROBABILITY = 0.8


def simulate_movement():
    """Simulate a robot movement with 80% success probability."""

    return random.random() < SUCCESS_PROBABILITY


def calculate_expected_cost(steps):
    """Calculate expected attempts for a route."""

    return steps / SUCCESS_PROBABILITY


def compare_routes(route_a, route_b):
    """Compare two routes using expected movement cost."""

    cost_a = calculate_expected_cost(route_a)
    cost_b = calculate_expected_cost(route_b)

    print("\nROUTE COMPARISON")
    print("-" * 40)

    print(f"Route A: {route_a} steps")
    print(f"Expected attempts: {cost_a:.2f}")

    print(f"\nRoute B: {route_b} steps")
    print(f"Expected attempts: {cost_b:.2f}")

    if cost_a < cost_b:
        selected = "Route A"
        reason = "Route A has the lower expected movement cost."
    elif cost_b < cost_a:
        selected = "Route B"
        reason = "Route B has the lower expected movement cost."
    else:
        selected = "Route A"
        reason = "Both routes have equal expected movement costs."

    print("\nSELECTED ROUTE:", selected)
    print("REASON:", reason)

    return selected, reason


def explanation_log():
    """Display the robot's decision explanation."""

    print("\nRESPONSIBLE AI EXPLANATION LOG")
    print("-" * 40)
    print("1. Movement success probability: 80%")
    print("2. Movement failure probability: 20%")
    print("3. Alternative routes are compared.")
    print("4. Expected movement costs are calculated.")
    print("5. The route with lower expected cost is selected.")
    print("6. The selection reason is displayed.")
    print("7. Robot movements should prioritize worker safety.")


def main():
    random.seed(42)

    print("=" * 45)
    print(" RESPONSIBLE AI - WAREHOUSE ROBOT PLANNER")
    print("=" * 45)

    print("\nUNCERTAIN MOVEMENT SIMULATION")
    print("-" * 40)

    for i in range(5):
        success = simulate_movement()

        if success:
            print(f"Movement {i + 1}: SUCCESS")
        else:
            print(f"Movement {i + 1}: FAILURE")

    print("\nENTER ROUTE INFORMATION")

    while True:
        try:
            route_a = int(input("Enter Route A length in steps: "))
            route_b = int(input("Enter Route B length in steps: "))

            if route_a <= 0 or route_b <= 0:
                print("Enter positive numbers.")
                continue

            break

        except ValueError:
            print("Please enter valid whole numbers.")

    compare_routes(route_a, route_b)
    explanation_log()

    print("\nPROJECT STATUS")
    print("-" * 40)
    print("BFS Navigation       : Implemented")
    print("CSP Task Assignment  : Implemented")
    print("STRIPS Actions       : Implemented")
    print("Multi-Robot Planning : Implemented")
    print("Responsible AI       : Demonstration implemented")

    print("\nResponsible AI demonstration completed!")


if __name__ == "__main__":
    main()