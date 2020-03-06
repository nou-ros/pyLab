#board
#display board
#play game
#handle turn
#check win
    #check rows
    #check columns
    #check diagnoals
#check tie
#flip players

#----- Global Variables -----


#1 
#game board
board = [
            "_", "_", "_",
            "_", "_", "_",
            "_", "_", "_"
        ]

# 10
# if game is still going
game_still_on = 1

# who won or tie
winner = None

# whose turn 
current_player = "X"

#2 Display board
def display_board():
    print()
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

#3
def play_game():

    #Display initial board
    display_board()

    #5play a game of tic tac toe
    while game_still_on:

        #handle a single turn of an arbitrary player
        handle_turn(current_player)

        #flip to other player
        flip_player()

        #check if the game has ended
        check_if_game_over()
        
        

#11
#the game has ended
    if winner == "X" or winner == "O":
        print()
        print(winner + " won.")
        print()
    elif winner == None:
        print()
        print("Tie.")
        print()

#4 handle a single turn of an arbitrary player
def handle_turn(player):
    print()
    print(player + " 's turn.")
    print()
    position = input("Choose a position from 1-9: ")
    
    valid = False
    while not valid:
        #17
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print()
            position = input("Choose a position from 1-9: ")

        #to get correct index for array
        position = int(position) - 1

        # 18 writing logic so occupied place will not be used again
        if board[position] == "_":
            valid = True
        else:
            print()
            print("Already occupied")

    board[position] = player

    display_board()

    return 

#6 
def check_if_game_over():
    check_if_win()
    check_if_tie()

#7
def check_if_win():

    #set up global vairables
    global winner

    #check rows
    row_winner = check_rows()

    #check columns
    column_winner = check_columns()

    #check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner

    elif column_winner:
        winner = column_winner
    
    elif diagonal_winner:
        winner = diagonal_winner

    else:
        winner = None

    return 

#12
def check_rows():
    #setup global variables
    global game_still_on 

    #check to see if rows have equal values
    row_1 = (board[0] == board[1] == board[2] != "_" )
    row_2 = (board[3] == board[4] == board[5] != "_" )
    row_3 = (board[6] == board[7] == board[8] != "_" )

    #if a match stop the game
    if row_1 or row_2 or row_3:
        game_still_on = 0

        #return the winner X or O
        if row_1:
            return board[0]
        elif row_2:
            return board[3]
        elif row_3:
            return board[6]
    return

# 13
def check_columns():
    #setup global variables
    global game_still_on 

    #check to see if rows have equal values
    column_1 = (board[0] == board[3] == board[6] != "_" )
    column_2 = (board[1] == board[4] == board[7] != "_" )
    column_3 = (board[2] == board[5] == board[8] != "_" )

    #if a match stop the game
    if column_1 or column_2 or column_3:
        game_still_on = 0

        #return the winner X or O
        if column_1:
            return board[0]
        elif column_2:
            return board[3]
        elif column_3:
            return board[6]
    return 

# 14
def check_diagonals():
    #setup global variables
    global game_still_on 

    #check to see if rows have equal values
    diagonal_1 = (board[0] == board[4] == board[8] != "_" )
    diagonal_2 = (board[6] == board[4] == board[2] != "_" )
    
    #if a match stop the game
    if diagonal_1 or diagonal_2:
        game_still_on = 0

        #return the winner X or O
        if diagonal_1:
            return board[0]
        elif diagonal_2:
            return board[6]
    return 

#8
def check_if_tie():
    # 16 
    global game_still_on 

    if "_" not in board:
        game_still_on = 0

    return 


#9
def flip_player():
 
    #15 global variable we need
    global current_player

    #change current player 
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    
    return 

play_game()