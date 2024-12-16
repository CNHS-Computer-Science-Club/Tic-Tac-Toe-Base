# True = P1, False = P2
turn = True

# 0 = O, 1 = X
board = [[" ", " ", " "], 
         [" ", " ", " "], 
         [" ", " ", " "]]

# Check if there's a winner or a tie
def check_winner():
    #check rows and columns for wins, then diagonals
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return f"Player 1 (X)" if row[0] == "X" else f"Player 2 (O)"
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return f"Player 1 (X)" if board[0][col] == "X" else f"Player 2 (O)"
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return f"Player 1 (X)" if board[0][0] == "X" else f"Player 2 (O)"
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return f"Player 1 (X)" if board[0][2] == "X" else f"Player 2 (O)"
    
    #check if there's no empty spaces
    for row in board:
        if " " in row:
            return None  #game continues
    
    return "Tie" #game ends

# Creates the board per turn
def new_turn():
    print("\n")
    for i in range(3):
        print(" " + str(board[i][0]) + " |  " + str(board[i][1]) + "  |  " + str(board[i][2]) + " ")
        if i < 2:
            print("-------------")
    print("\n")

# Take player input
def take_input():
    global turn
    while True:
        if turn:
            print("Player 1's turn (X)")
        else:
            print("Player 2's turn (O)")
        try:
            # Prompt the user for input in "row,col" format
            input_string = input("Enter your move as 'row,col' (e.g., 0,1): ").strip()
            
            # Split the input string and parse it into integers
            row, col = map(int, input_string.split(","))
            
            # Check if the coordinates are valid and the spot is empty
            if 0 <= row < 3 and 0 <= col < 3:  # Ensure the coordinates are within bounds
                if board[row][col] == " ":
                    # Assign 'X' or 'O' based on the turn
                    board[row][col] = "X" if turn else "O"
                    
                    # Toggle the turn
                    turn = not turn
                    break
                else:
                    print("Invalid move! That spot is already taken. Try again.")
            else:
                print("Invalid input! Coordinates must be between 0 and 2. Try again.")
        except (ValueError, IndexError):
            print("Invalid input! Please enter your move as 'row,col'. For example: 0,1.")

# Reset the game
def reset_game():
    global board, turn
    board = [[" ", " ", " "] for _ in range(3)]
    turn = True
    print("Game reset!")

# Main game loop
def play_game():
    reset_game()
    while True:
        new_turn()
        take_input()
        result = check_winner()
        if result:
            new_turn()
            if result == "Tie":
                print("It's a tie!")
            else:
                print(f"{result} wins!")
            break

play_game()
