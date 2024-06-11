#  GAME TIC TAC TOE with User Interaction, Turn Management and Win Condition checking.
import os
import sys

def pos_table():
    print("Displaying the corresponding position numbers")
    print("{0:4}|{1:^5}|{2:>4}".format(7, 8, 9))
    print('_______________')
    print("{0:4}|{1:^5}|{2:>4}".format(4, 5, 6))
    print('_______________')
    print("{0:4}|{1:^5}|{2:>4}".format(1, 2, 3))

#displayboard by name
def displayboard(board):
    os.system('cls')
    print("{0:4}|{1:^5}|{2:>4}".format(board[7], board[8], board[9]))
    print('_______________')
    print("{0:4}|{1:^5}|{2:>4}".format(board[4], board[5], board[6]))
    print('_______________')
    print("{0:4}|{1:^5}|{2:>4}".format(board[1], board[2], board[3]))
    gamestatus(board)

def marker(mark):
    if start() == mark:
        return 'player 1'
    else:
        return 'player 2'

#Asks the user to confirm the exit status
def game_exit(board):
    user_in = input("Are u sure u want to exit the game? Enter 'N' to CONTINUE or To confirm EXIT enter 'Y'").upper()
    if(user_in == 'Y'):
        sys.exit("Thank u for playing")
    else:
        update_board(board)

#A function to check the status {win/draw/exit/continue} the game
def gamestatus(board):
    global count
    m = count%2
    count += 1
    if board_check(board):
        print('The game is a DRAW')
        replay()
    elif m == 0:
        if board_win(board, 'O'):
            print(f"The winner is O. Congratulations {marker('O')}")
            replay()
        else:
            update_board(board)
    else:
        if board_win(board, 'X'):
            print(f"The winner is X. Congratulations {marker('X')}")
            replay()
        else:
            update_board(board)

#maintains the count globally
count = 1
#update_board prompts user and also updates the board.
def update_board(board):
    pos = 0
    inp = ''
    
    while(pos not in range(1,10) or not space_check(pos,board)):
        if count%2 == 0: 
            print("O's turn!")
        else:
            print("X's turn!")
        pos = int(input("Enter the position u wanna place ur letter: "))
        if(pos == -1):
            rules(board)
    
    if count%2 == 0:
        board[pos] = 'O'
    else:
        board[pos] = 'X'
    displayboard(board)

def board_win(board, mark):
    for i in [1,4,7]:
        if board[i] == board[i+1] == board[i+2] == mark:
            return True
    for i in range(1,4):
        if board[i] == board[i+3] == board[i+6] == mark:
            return True
    if board[1] == board[5] == board[9] == mark:
        return True
    if board[3] == board[5] == board[7] == mark:
        return True
    
    return False

#Checks wthether space is there or not
def space_check(position, board):
    return board[position] == ' '

#Checks wthether the board is full or not
def board_check(board):
    for a in range(1, 10):
        if space_check(a,board) == True:
            return False
    return True

def start():
    c = 'a'
    print('Enter -1 to display player options')
    while c:
        user_inp = input("Player 1 choose ur letter 'X' or 'O': ")
        c = user_inp.upper()
        if(c == 'X' or c == 'O'):
            break
    #Displaying initial table
    pos_table()
    #Starts the function loops!!
    update_board(board)
    return c
    
def rules(board):
    lst = ['Enter 3 to exit','Enter 2 to continue', 'Enter 1 to view Position Table']
    if count == 1:
        start()
    else:
        for l in lst:
            print(l)
    i = int(input("Enter a number: "))
    if(i == 3):
        game_exit(board)
    elif(i == 1):
        pos_table()
    elif(i == 2):
        update_board(board)

#Asks user wthether wants to play again or exit   
def replay():
    ans = input("Do u like to play again? 'Yes' or 'No'").lower()[0]
    if ans == 'y':
        start()
    else:
        sys.exit("Thank u for playing")

#main function starts here
#First let's print the basic user prompt at start
os.system('cls')
print("{0:>75}".format('WELCOME TO TIC TAC TOE!'))
board = [' ']*10
rules(board)


