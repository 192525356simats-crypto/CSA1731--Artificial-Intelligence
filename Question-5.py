import itertools

def get_value(word, mapping):
    """Converts a word into its integer value based on the letter-to-digit mapping."""
    value = 0
    for char in word:
        value = value * 10 + mapping[char]
    return value

def solve_cryptarithmetic(equation):
    # Clean and parse the equation (e.g., "SEND + MORE = MONEY")
    left, right = equation.upper().replace(" ", "").split("=")
    addends = left.split("+")
    
    # Extract all unique letters
    unique_letters = sorted(list(set(right + "".join(addends))))
    if len(unique_letters) > 10:
        print("Invalid puzzle: More than 10 unique letters.")
        return

    # Identify leading letters (first letter of each multi-digit word cannot be 0)
    leading_letters = {word[0] for word in addends + [right] if len(word) > 1}

    # Test all possible digit assignments
    for perm in itertools.permutations(range(10), len(unique_letters)):
        mapping = dict(zip(unique_letters, perm))
        
        # Skip if any leading letter is assigned 0
        if any(mapping[letter] == 0 for letter in leading_letters):
            continue
        
        # Calculate sums and check if the equation holds
        if sum(get_value(word, mapping) for word in addends) == get_value(right, mapping):
            print(f"Solution for: {equation}")
            print("Mapping:", mapping)
            
            # Format and display the numeric equation
            left_nums = " + ".join(str(get_value(w, mapping)) for w in addends)
            right_num = str(get_value(right, mapping))
            print(f"Equation: {left_nums} = {right_num}\n")
            return

    print("No solution found.")

# Example Usage
if __name__ == "__main__":
    solve_cryptarithmetic("SEND + MORE = MONEY")
    solve_cryptarithmetic("TWO + TWO = FOUR")
