# Multi-Robot Warehouse Planner - STRIPS Actions
# Preconditions, effects, and safety rules


class Robot:
    def __init__(self):
        self.position = (0, 0)
        self.has_product = False
        self.battery = 100
        self.forbidden_cells = set()

    def human_nearby(self, cell):
        """Safety rule: HumanNearby(c) -> Forbidden(c)."""
        return cell in self.forbidden_cells

    def move(self, new_position):
        # Preconditions
        if self.battery <= 0:
            print("Move failed: Battery is empty.")
            return False

        if self.human_nearby(new_position):
            print("Move failed: Cell forbidden due to nearby human.")
            return False

        # Effects
        self.position = new_position
        self.battery -= 1

        print(f"Move: Robot moved to {self.position}")
        return True

    def pick(self):
        # Preconditions
        if self.has_product:
            print("Pick failed: Robot already has a product.")
            return False

        # Effects
        self.has_product = True

        print("Pick: Product picked up.")
        return True

    def drop(self):
        # Preconditions
        if not self.has_product:
            print("Drop failed: No product to deliver.")
            return False

        # Effects
        self.has_product = False

        print("Drop: Product delivered.")
        return True

    def charge(self):
        # Effects
        self.battery = 100

        print("Charge: Battery restored to 100%.")
        return True


if __name__ == "__main__":
    robot = Robot()

    print("ROBOT STRIPS ACTIONS")
    print("-" * 30)

    # Add a safety restriction for cell (0, 2)
    robot.forbidden_cells.add((0, 2))

    robot.move((0, 1))
    robot.pick()

    # This move should be blocked by the safety rule
    robot.move((0, 2))

    # Use a safe alternative cell
    robot.move((1, 1))
    robot.drop()
    robot.charge()

    print("\nFinal Position:", robot.position)
    print("Product Status:", robot.has_product)
    print("Battery:", robot.battery, "%")