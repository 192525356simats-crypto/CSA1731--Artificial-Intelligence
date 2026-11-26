import heapq

def heuristic(a, b):
    """Calculate the Manhattan distance between two points."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    
    # Priority queue storing tuples of (f_score, current_node)
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    # Dictionary to reconstruct the shortest path
    came_from = {}
    
    # Cost from start to each node (defaulting to infinity)
    g_score = {start: 0}
    
    # Total estimated cost from start to goal through each node
    f_score = {start: heuristic(start, goal)}
    
    # Directions: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while open_set:
        # Pop the node with the lowest f_score
        _, current = heapq.heappop(open_set)
        
        # Goal reached: reconstruct and return the path
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Reverse to get start -> goal
        
        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)
            
            # Check grid boundaries and obstacles (1 = wall)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if grid[neighbor[0]][neighbor[1]] == 1:
                    continue
                
                # Distance between adjacent cells is 1
                tentative_g_score = g_score[current] + 1
                
                # If this path to neighbor is better than any previous one
                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f = tentative_g_score + heuristic(neighbor, goal)
                    f_score[neighbor] = f
                    heapq.heappush(open_set, (f, neighbor))
                    
    return None  # No path exists

# --- Example Usage ---
if __name__ == "__main__":
    # 0 = Walkable path, 1 = Obstacle
    grid_map = [
        [0, 0, 0, 0, 1],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    
    start_pos = (0, 0)
    goal_pos = (4, 4)
    
    shortest_path = a_star_search(grid_map, start_pos, goal_pos)
    
    if shortest_path:
        print("Shortest Path:", shortest_path)
    else:
        print("No path found.")
