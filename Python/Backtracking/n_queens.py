def is_complete_solution(solution, n):
    # Solution is complete if we have placed N queens
    return len(solution) == n


def is_valid(candidate, solution):
    # Check if the queen placement is valid or not
    row, col = candidate
    for r, c in solution:
        if c == col or abs(r - row) == abs(c - col):  # Same column or diagonal
            return False
    return True


def generate_candidate(solution, n):
    # The current row where a queen needs to be placed
    row = len(solution)
    # Try all columns in the current row
    return [(row, col) for col in range(n)]


def process_solution(solution, solutions):
    # Append the valid solution to the solutions list
    solutions.append(solution[:])  # Add a copy of the solution


def n_queens(n):
    solutions = []  # To store all valid solutions

    def backtrack(solution):
        # Check if we found a solution
        if is_complete_solution(solution, n):
            # Save the solution
            process_solution(solution, solutions)
            return
        # Explore the candidates
        for candidate in generate_candidate(solution, n):
            if is_valid(candidate, solution):
                solution.append(candidate)  # Choose
                backtrack(solution=solution)  # Explore
                solution.pop()  # Undo (backtrack)

    backtrack([])  # Start with an empty solution
    return solutions  # Return the list of all valid solutions


# Get all solutions for n=4 queens
solutions = n_queens(4)

# Print all solutions
for idx, solution in enumerate(solutions):
    print(f"Solution {idx + 1}: {solution}")
