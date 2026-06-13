def print_board(board):
    print("\n")
    for row in board:
        # This joins the items in the row with a " | " separator
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_winner(board, player):
    # Check rows
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            return True
            
    # Check columns
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
            
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
        
    return False

def check_tie(board):
    for row in board:
        # If there is even one empty spot, the board is not full
        if "-" in row:
            return False
    # If the loop finishes without finding a "-", the board is full
    return True

# --- Main Game Setup ---
# Creating the 3x3 grid using a 2D list
board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

current_player = "X"
print("Welcome to Tic Tac Toe!")
print_board(board)

# --- Main Game Loop ---
while True:
    print("Player " + current_player + "'s turn.")
    
    # Using a try/except block in case the user types a letter instead of a number
    try:
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))
    except ValueError:
        print("Invalid input! Please enter a number.\n")
        continue

    # 1. Check if input is within the 0-2 range
    if row < 0 or row > 2 or col < 0 or col > 2:
        print("Invalid choice! Choose a number between 0 and 2.\n")
        continue
        
    # 2. Check if the chosen spot is already taken
    if board[row][col] != "-":
        print("That spot is already taken! Try again.\n")
        continue

    # Update the board with the player's move
    board[row][col] = current_player
    print_board(board)

    # Check if the current player just won
    if check_winner(board, current_player):
        print("Congratulations! Player " + current_player + " wins!")
        break
        
    # Check if the board is full (a tie)
    if check_tie(board):
        print("It's a tie game!")
        break

    # Switch turns
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
