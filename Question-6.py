from collections import deque

def is_valid(m_left, c_left):
    # Check bounds (0 to 3 people on the left bank)
    if m_left < 0 or c_left < 0 or m_left > 3 or c_left > 3:
        return False
    
    # Calculate people on the right bank
    m_right = 3 - m_left
    c_right = 3 - c_left
    
    # Missionaries cannot be outnumbered by cannibals on either bank
    if m_left > 0 and c_left > m_left:
        return False
    if m_right > 0 and c_right > m_right:
        return False
        
    return True

def solve_missionaries_cannibals():
    # State format: (missionaries_left, cannibals_left, boat_position)
    # boat_position: 1 = Left Bank, 0 = Right Bank
    start_state = (3, 3, 1)
    goal_state = (0, 0, 0)
    
    # Queue stores tuples of (current_state, path_taken)
    queue = deque([(start_state, [start_state])])
    visited = set([start_state])
    
    # Possible boat moves: (missionaries, cannibals)
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    
    while queue:
        (m_left, c_left, boat), path = queue.popleft()
        
        # Check if goal is reached
        if (m_left, c_left, boat) == goal_state:
            return path
        
        for m_move, c_move in moves:
            if boat == 1:  # Boat is on the left bank, moving to the right
                new_state = (m_left - m_move, c_left - c_move, 0)
            else:          # Boat is on the right bank, moving to the left
                new_state = (m_left + m_move, c_left + c_move, 1)
                
            if is_valid(new_state[0], new_state[1]) and new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [new_state]))
                
    return None

def print_solution(solution):
    if not solution:
        print("No solution found.")
        return
        
    print(f"Solution found in {len(solution) - 1} moves:\n")
    print("Left Bank (M, C)  |  Boat   |  Right Bank (M, C)")
    print("-" * 50)
    for m_left, c_left, boat in solution:
        m_right, c_right = 3 - m_left, 3 - c_left
        boat_pos = "Left " if boat == 1 else "Right"
        print(f"     ({m_left}, {c_left})       |  {boat_pos}  |       ({m_right}, {c_right})")

if __name__ == "__main__":
    solution = solve_missionaries_cannibals()
    print_solution(solution)
