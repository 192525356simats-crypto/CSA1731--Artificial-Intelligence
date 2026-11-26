import random


class VacuumCleanerAgent:

  def __init__(self):
    self.performance_score = 0

  def perceive_and_act(self, location, status):
    """Decides the next action based on current location and cleanliness."""
    if status == "Dirty":
      return "Suck"
    elif location == "A":
      return "MoveRight"
    elif location == "B":
      return "MoveLeft"


def run_simulation():
  # Randomly initialize the environment ('Clean' or 'Dirty')
  environment = {
      "A": random.choice(["Clean", "Dirty"]),
      "B": random.choice(["Clean", "Dirty"]),
  }

  # Randomly place the vacuum in Room A or Room B
  current_location = random.choice(["A", "B"])
  agent = VacuumCleanerAgent()

  print(f"Initial Environment: {environment}")
  print(f"Vacuum starting at: Room {current_location}\n")

  # Run the agent for enough steps to guarantee both rooms are checked and cleaned
  for step in range(1, 5):
    current_status = environment[current_location]
    action = agent.perceive_and_act(current_location, current_status)

    print(
        f"Step {step}: Location = {current_location}, Status ="
        f" {current_status} -> Action: {action}"
    )

    # Execute the chosen action in the environment
    if action == "Suck":
      environment[current_location] = "Clean"
      agent.performance_score += 10  # Reward for cleaning dirt
    elif action == "MoveRight":
      current_location = "B"
      agent.performance_score -= 1  # Small penalty for movement cost
    elif action == "MoveLeft":
      current_location = "A"
      agent.performance_score -= 1

    # Stop early if both rooms are already clean
    if environment["A"] == "Clean" and environment["B"] == "Clean":
      print("\nAll rooms are clean!")
      break

  print(f"Final Environment: {environment}")
  print(f"Performance Score: {agent.performance_score}")


if __name__ == "__main__":
  run_simulation()
