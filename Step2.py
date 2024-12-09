#true = P1, false = P2
turn = True
game = True

#0 = O, 1 = X
board = [[" ", " ", " "], 
         [" ", " ", " "], 
         [" ", " ", " "]]
         
#check_board for winners
def check_board():
    pass

#creates board per turn
def new_turn():
    #empty board:
    # print("   |     |    ")
    # print("-------------")
    # print("   |     |    ")
    # print("-------------")
    # print("   |     |    ")
    
    #row 1
    print(" " + str(board[0][0]) + " |  " + str(board[0][1]) + "  |  " + str(board[0][2]) + " ")
    
    print("-------------")
    
    #row 2
    print(" " + str(board[1][0]) + " |  " + str(board[1][1]) + "  |  " + str(board[1][2]) + " ")
    
    print("-------------")
    
    #row 3
    print(" " + str(board[2][0]) + " |  " + str(board[2][1]) + "  |  " + str(board[2][2]) + " ")

def take_input():
    global turn
    while True:
        if turn:
            print("Player 1's turn (X)")
        else:
            print("Player 2's turn (O)")
        try:
            # Prompt the user for input in "row,col" format
            input_string = input("Enter your move as 'row,col' e.g., 0,1 : ").strip()
            
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
    

#resets game
def reset_game():
    pass

while(game):
    take_input()
    new_turn()

