import heapq

GOAL_STATE = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)  # 0 represents the blank tile
)

def manhattan_distance(state):
    distance = 0
    for r in range(3):
        for c in range(3):
            val = state[r][c]
            if val != 0:
                target_r, target_c = (val - 1) // 3, (val - 1) % 3
                distance += abs(r - target_r) + abs(c - target_c)
    return distance

def get_neighbors(state):
    neighbors = []
    # Find the blank tile (0)
    zero_r, zero_c = next(
        (r, c) for r in range(3) for c in range(3) if state[r][c] == 0
    )
    moves = [(-1, 0, "Up"), (1, 0, "Down"), (0, -1, "Left"), (0, 1, "Right")]

    for dr, dc, action in moves:
        new_r, new_c = zero_r + dr, zero_c + dc
        if 0 <= new_r < 3 and 0 <= new_c < 3:
            board = [list(row) for row in state]
            board[zero_r][zero_c], board[new_r][new_c] = (
                board[new_r][new_c],
                board[zero_r][zero_c],
            )
            neighbors.append((tuple(tuple(row) for row in board), action))
    return neighbors

def solve_8_puzzle(start_state):
    priority_queue = []
    # (f_score, g_score, current_state, path)
    heapq.heappush(priority_queue, (manhattan_distance(start_state), 0, start_state, []))
    visited = set()

    while priority_queue:
        f_score, g_score, current_state, path = heapq.heappop(priority_queue)

        if current_state == GOAL_STATE:
            return path

        if current_state in visited:
            continue
        visited.add(current_state)

        for next_state, action in get_neighbors(current_state):
            if next_state not in visited:
                new_g = g_score + 1
                new_f = new_g + manhattan_distance(next_state)
                heapq.heappush(
                    priority_queue, (new_f, new_g, next_state, path + [(action, next_state)])
                )
    return None

# Example Usage
initial_board = (
    (1, 2, 3),
    (4, 0, 6),
    (7, 5, 8)
)

solution = solve_8_puzzle(initial_board)

if solution:
    print(f"Solved in {len(solution)} moves:\n")
    for step, (move, board) in enumerate(solution, 1):
        print(f"Step {step}: Move {move}")
        for row in board:
            print(row)
        print()
else:
    print("No solution exists for the given state.")
