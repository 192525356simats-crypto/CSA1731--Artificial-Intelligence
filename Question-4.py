from collections import deque


def solve_water_jug(cap1, cap2, target):
    # Check if the target is mathematically possible
    if target > max(cap1, cap2):
        return None

    # Queue stores tuples of: (current_jug1, current_jug2, path_taken)
    queue = deque([(0, 0, [(0, 0)])])
    visited = set([(0, 0)])

    while queue:
        jug1, jug2, path = queue.popleft()

        # Goal check: either jug contains the exact target amount
        if jug1 == target or jug2 == target:
            return path

        # Generate all 6 possible next states
        next_states = [
            (cap1, jug2),  # 1. Fill Jug 1
            (jug1, cap2),  # 2. Fill Jug 2
            (0, jug2),  # 3. Empty Jug 1
            (jug1, 0),  # 4. Empty Jug 2
            # 5. Pour Jug 1 into Jug 2
            (
                jug1 - min(jug1, cap2 - jug2),
                jug2 + min(jug1, cap2 - jug2),
            ),
            # 6. Pour Jug 2 into Jug 1
            (
                jug1 + min(jug2, cap1 - jug1),
                jug2 - min(jug2, cap1 - jug1),
            ),
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state[0], state[1], path + [state]))

    return None


# Example Usage: 4-liter jug, 3-liter jug, target of 2 liters
capacity_1 = 4
capacity_2 = 3
goal = 2

solution = solve_water_jug(capacity_1, capacity_2, goal)

if solution:
    print(
        f"Shortest solution to measure {goal}L using {capacity_1}L and"
        f" {capacity_2}L jugs:"
    )
    for step, state in enumerate(solution):
        print(f"Step {step}: Jug 1 = {state[0]}L, Jug 2 = {state[1]}L")
else:
    print("No solution possible.")
