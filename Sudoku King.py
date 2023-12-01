def is_valid(board, row, col, num):
    # Check if the number is not present in the current row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check if the number is not present in the current 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty_location(board):
    # Find the first empty cell in the puzzle
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def solve_sudoku(board):
    # Find an empty location in the puzzle
    empty_location = find_empty_location(board)

    # If there is no empty location, the puzzle is solved
    if not empty_location:
        return True

    row, col = empty_location

    # Try placing a number from 1 to 9
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            # If the number is valid, place it in the puzzle
            board[row][col] = num

            # Recursively try to solve the remaining puzzle
            if solve_sudoku(board):
                return True

            # If placing the number doesn't lead to a solution, backtrack
            board[row][col] = 0

    # If no number from 1 to 9 can be placed, backtrack to the previous state
    return False

def print_sudoku(board):
    for row in board:
        print(" ".join(map(str, row)))

def get_user_input():
    board = []
    print("Enter the Sudoku puzzle (use 0 for empty cells):")
    for _ in range(9):
        row = list(map(int, input().split()))
        board.append(row)
    return board

if __name__ == "__main__":
    sudoku_board = get_user_input()

    print("\nSudoku Puzzle:")
    print_sudoku(sudoku_board)

    if solve_sudoku(sudoku_board):
        print("\nSolved Sudoku:")
        print_sudoku(sudoku_board)
    else:
        print("\nNo solution exists.")
