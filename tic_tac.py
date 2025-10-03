from random import randrange

# Step 1
def display_board(board):
    horizontal_line = "+-------" * 3 + "+"
    empty_line = "|       " * 3 + "|"

    for row in board:
        print(horizontal_line)
        print(empty_line)
        print("|", end="")
        for cell in row:
            print(f"   {cell}   |", end="")
        print()
        print(empty_line)
    print(horizontal_line)

# Step 2
def enter_move(board):
    move = input("Enter your move (1-9): ")
    if move.isdigit():
        move = int(move)
        if 1 <= move <= 9:
            row = (move - 1) // 3
            col = (move - 1) % 3
            if board[row][col] not in ['X', 'O']:
                board[row][col] = 'O'
            else:
                print("Cell already taken.")
        else:
            print("Move out of range.")
    else:
        print("Invalid input. Please enter a number.")

# Step 3
def make_list_of_free_fields(board):
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] != 'X' and board[row][col] != 'O':
                free_fields.append((row, col))
    return free_fields

# Step 4
def victory_for(board, sign):
    for row in board:
        if row[0] == row[1] == row[2] == sign:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == sign:
            return True
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    return False

# Step 5
def draw_move(board):
    free_fields = make_list_of_free_fields(board)

    # Try to win
    for row, col in free_fields:
        board[row][col] = 'X'
        if victory_for(board, 'X'):
            return
        board[row][col] = row * 3 + col + 1  # Undo move

    # Try to block player
    for row, col in free_fields:
        board[row][col] = 'O'
        if victory_for(board, 'O'):
            board[row][col] = 'X'
            return
        board[row][col] = row * 3 + col + 1  # Undo move

    # Otherwise, pick random
    index = randrange(len(free_fields))
    row, col = free_fields[index]
    board[row][col] = 'X'


# Main game loop
def main():
    board = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

    board[1][1] = 'X'  # First move by computer
    display_board(board)

    while True:
        enter_move(board)
        display_board(board)
        if victory_for(board, 'O'):
            print("You won!")
            break
        if not make_list_of_free_fields(board):
            print("It's a tie!")
            break

        draw_move(board)
        display_board(board)
        if victory_for(board, 'X'):
            print("Computer won!")
            break
        if not make_list_of_free_fields(board):
            print("It's a tie!")
            break

# Run the game
main()


