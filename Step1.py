#true = P1, false = P2
turn = True

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

#resets game
def reset_game():
    pass

new_turn()
