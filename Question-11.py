import heapq

def heuristic(a, b):
    """Calculate the Manhattan distance between two points."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(grid, start, goal):
    """
    Find the shortest path in a 2D grid using the A* algorithm.
    0 represents an open cell, 1 represents an obstacle/wall.
    """
    rows, cols = len(grid), len(grid[0])
    
    # Priority queue storing tuples of (f_score, current_node)
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    # Dictionaries to track the path and g_scores
    came_from = {}
    g_score = {start: 0}
    
    # 4-directional movement (Up, Down, Left, Right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while open_set:
        # Pop the node with the lowest f_score
        current_f, current = heapq.heappop(open_set)
        
        # If the goal is reached, reconstruct and return the path
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Reverse to get start -> goal order
        
        # Explore neighbors
        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)
            
            # Check grid boundaries and obstacles
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if grid[neighbor[0]][neighbor[1]] == 1:
                    continue  # Skip walls
                
                # Each step has a cost of 1
                tentative_g_score = g_score[current] + 1
                
                # If this path to the neighbor is better than any previous one
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score, neighbor))
                    
    return None  # Return None if no path exists

# --- Example Usage ---
if __name__ == "__main__":
    # 0 = Walkable path, 1 = Obstacle
    maze = [
        [0, 0, 0, 0, 1],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    
    start_pos = (0, 0)
    goal_pos = (4, 4)
    
    shortest_path = a_star_search(maze, start_pos, goal_pos)
    
    if shortest_path:
        print("Shortest Path:", shortest_path)
        print("Total Steps:", len(shortest_path) - 1)
    else:
        print("No path found.")
