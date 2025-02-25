import time

def read_sudoku_from_file(file_path):
    """Reads Sudoku puzzle from a file and creates list."""
    with open(file_path, "r") as file:
        return [[int(num) for num in line.strip()] for line in file.readlines()]

def is_safe(mat, row, col, num):
    """Check if it's safe to place a number in a given cell."""
    for x in range(9):
        if mat[row][x] == num or mat[x][col] == num:
            return False
    
    start_row, start_col = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if mat[start_row + i][start_col + j] == num:
                return False
    return True

def display_sudoku(mat):
    """Displays the Sudoku puzzle in a formatted manner."""
    print("+-------+-------+-------+")
    for i, row in enumerate(mat):
        print("| " + " ".join(str(num) if num != 0 else '.' for num in row[:3]) + " | " +
              " ".join(str(num) if num != 0 else '.' for num in row[3:6]) + " | " +
              " ".join(str(num) if num != 0 else '.' for num in row[6:]) + " |")
        if (i + 1) % 3 == 0:
            print("+-------+-------+-------+")

def solve_sudoku_rec(mat, row, col, attempt_counter):
    """Recursive function to solve Sudoku using backtracking, displaying each attempt."""
    if row == 8 and col == 9:
        return True
    if col == 9:
        row += 1
        col = 0
    if mat[row][col] != 0:
        return solve_sudoku_rec(mat, row, col + 1, attempt_counter)
    
    for num in range(1, 10):
        if is_safe(mat, row, col, num):
            mat[row][col] = num
            attempt_counter[0] += 1
            print(f"Attempt {attempt_counter[0]}:")
            display_sudoku(mat)
            if solve_sudoku_rec(mat, row, col + 1, attempt_counter):
                return True
            mat[row][col] = 0
    return False

def solve_sudoku(file_path):
    """Reads a file, solves it, and prints result."""
    mat = read_sudoku_from_file(file_path)
    attempt_counter = [0]
    
    print("Initial Sudoku Puzzle:")
    display_sudoku(mat)
    
    start_time = time.time()
    
    if solve_sudoku_rec(mat, 0, 0, attempt_counter):
        print("Final Solution:")
        display_sudoku(mat)
    else:
        print("No solution exists")
    
    end_time = time.time()
    
    print(f"Total attempts: {attempt_counter[0]}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    file_path = "/Users/alexander.tully26/Downloads/20250107-nyt-easy.sudoku"
    solve_sudoku(file_path)
