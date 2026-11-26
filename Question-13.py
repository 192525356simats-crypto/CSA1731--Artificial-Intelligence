# Define the CSP components: Variables, Domains, and Constraints (Neighbors)
variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']

domains = {
    var: ['Red', 'Green', 'Blue'] for var in variables
}

# Adjacency list representing the constraints (adjacent regions cannot share a color)
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []  # Tasmania has no land borders
}

def is_consistent(variable, color, assignment):
    """Check if assigning 'color' to 'variable' violates any neighbor constraints."""
    for neighbor in neighbors[variable]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def select_unassigned_variable(assignment):
    """Select the next variable that has not yet been assigned a color."""
    for var in variables:
        if var not in assignment:
            return var
    return None

def backtrack(assignment):
    """Recursive backtracking algorithm to solve the CSP."""
    # Base case: if all variables are assigned, return the complete assignment
    if len(assignment) == len(variables):
        return assignment

    var = select_unassigned_variable(assignment)

    for color in domains[var]:
        if is_consistent(var, color, assignment):
            # Assign color
            assignment[var] = color
            
            # Recursively assign remaining variables
            result = backtrack(assignment)
            if result is not None:
                return result
            
            # Backtrack if assignment leads to a dead end
            del assignment[var]

    return None

# Driver Code
if __name__ == "__main__":
    solution = backtrack({})
    
    if solution:
        print("Valid Map Coloring Solution:")
        for region, color in solution.items():
            print(f"{region}: {color}")
    else:
        print("No valid solution found.")
