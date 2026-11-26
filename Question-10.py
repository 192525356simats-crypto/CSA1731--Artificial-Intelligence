from itertools import permutations
import math

def calculate_tsp(distance_matrix, start_city=0):
    num_cities = len(distance_matrix)
    cities = list(range(num_cities))
    
    # Exclude the starting city from the list of cities to permute
    cities.remove(start_city)
    
    min_distance = math.inf
    best_path = []
    
    # Generate all possible permutations of the remaining cities
    for perm in permutations(cities):
        current_path = [start_city] + list(perm) + [start_city]
        current_distance = 0
        
        # Calculate total distance of the current path
        for i in range(len(current_path) - 1):
            from_city = current_path[i]
            to_city = current_path[i + 1]
            current_distance += distance_matrix[from_city][to_city]
            
        # Update the best path if a shorter route is found
        if current_distance < min_distance:
            min_distance = current_distance
            best_path = current_path
            
    return min_distance, best_path

if __name__ == "__main__":
    # Example distance matrix where matrix[i][j] is the distance from city i to city j
    # 0: City A, 1: City B, 2: City C, 3: City D
    example_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    starting_point = 0
    min_dist, path = calculate_tsp(example_matrix, start_city=starting_point)
    
    print("--- Traveling Salesman Problem (Brute Force) ---")
    print(f"Optimal Path: {' -> '.join(map(str, path))}")
    print(f"Minimum Distance: {min_dist}")
