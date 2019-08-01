# Program Battleship
# Description: 
#   	A game of battleship
# Author: Jacob Reola 
# Date: 19 October 2017
# Revised: 
# 16 December 2017 

# list libraries used
import random

# Declare global constants
COLUMNS = ['# ', ' A ', ' B ', ' C ', ' D ', ' E ', ' F ', ' G ', ' H ', ' I ', ' J ']
COLUMN_INDICES = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
ROW_CHOICES = ['0', '1', '2', '3', '4' ,'5', '6', '7', '8', '9']     
MAX_ROW = 10
MAX_COL = 10
COMPUTER_SHIP = ' 8 '
PLAYER_SHIP = ' 1 '
HIT = ' X '
MISS = ' M '
STAR = ' * '



def main():

    # declare variables
    computer_board = []  # what's seen reflects hit or miss
    player_board = []    # where the player ship is located 
    hidden_computer_board = []   # stores where the ships are
    max_player_hits = 0
    enemy_ships = 0

    # This begins the game
    print ('Welcome to battleship.')
    print ('Let the game begin!')

    # This allows the player to play again after the game ends
    play_again = True

    # begins loop to play again after end game.
    while(play_again):

        # calls play_Game function using player_lose as a variable
        player_lose = play_Game(enemy_ships, max_player_hits, computer_board, player_board,hidden_computer_board)

        # begins if statement 
        if(player_lose):

            # prompts user to play again
            choice = input("You lost, do you want to play again? Y/N  ")

            # Loops the user input choice to play 
            while(choice != 'Y' and choice != 'N'):
                choice = input("Your choice is not valid, input Y for yes, N for no  "  )

            # End While

            # gives the user a choice to play again with boolean value
            if(choice == 'Y'):
                play_again = True
                
            else:
                play_again = False

            # End if

        # End while
               
        else:
            choice = input("You won! Do you want to play again? Y/N    " )

            while(choice != 'Y' and choice != 'N'):
                choice = input("Your choice is not valid, input Y for yes, N for no  ")

            # End while
            
            if(choice == 'Y'):
                play_again = True
            else:
                play_again = False

            # End if 

        # End if
    print("Bye - bye! Thanks for playing")

# Function play_Game
# Description:
#	This displays the board and peices
# Calls:
#	setup_board()
# Parameters:
#	comp_ships  Integer
#       player_ships    Integer
#       comp_board  2D list
#       player_board    2D list
#       hidden_comp_board   2D list
# Returns:
#	player_ships     Integer
   
def play_Game(comp_ships, player_ships, comp_board, player_board, hidden_comp_board ):

    # These are function calls of setup_board
    comp_board = setup_board()
    hidden_comp_board = setup_board()
    player_board = setup_board()

    # This function displays the board
    display_board (comp_board)

    # this keeps track of the computer ships on the board and doesn't display location
    comp_ships = enemy_ships(hidden_comp_board)
    
    # this is the formula to determine the amount of hits the player can recieve
    player_ships = round(comp_ships/2)

    # The x, y randomly chooses a location on the board
    x = random.choice(list(COLUMN_INDICES))
    y = random.randint(0, 9)

    # displays the postion of the ship 
    print ('Your location is at', x,y,'.')

    # displays the amount of hits the player can take and updates per turn
    print ('Your ship can take', player_ships, 'hits.')

    # the x changes into a corresponding number from the dict.
    x = COLUMN_INDICES[x]

    # This actually puts the player ship on the board
    player_board[y][x] = PLAYER_SHIP

    # loops the game after their is a winner/loser to play again
    while(comp_ships!= 0 and player_ships != 0):
        print("IT'S PLAYER'S TURN")
        print()

        # this prompts the user to choose a column
        x = input("Choose column letter( A - J )  ")

        # begins loop and corrects user from improper input
        while (x not in COLUMN_INDICES.keys()):
            x = input("Choice is not valid, please choose from A to J, case sensitive  ")

        # end while

        # prompts user to input row
        y = input("Choose row number(0 - 9)  ")

        # begins loop and corrects user from improper input
        while (y not in ROW_CHOICES):          
            y = input("Choice is not valid, please choose from 0 to 9  ")
            
        # This x,y variable updates after every use input
        x = COLUMN_INDICES[x]
        y = int(y)

        # this determines if the user input hits a computer ship
        hit = (hidden_comp_board[y][x] == COMPUTER_SHIP)

        # this happens if user hits the computer ship
        if (hit) :
            print("You hit one of the enemy ships!")
            print()

            # updates the computer board and hidden computer board after every hit
            comp_board[y][x] = HIT
            hidden_comp_board[y][x] = HIT

            # computer ships are updated after every hit
            comp_ships = comp_ships - 1
        else:
            print("You did not hit a ship.")
            print()
            comp_board[y][x] = MISS

        # end if

        # if the computer lost, while loop breaks and ends game
        if(comp_ships == 0):
            break
        print("CURRENT COMPUTER BOARD: ", comp_ships, "SHIPS REMAINING")
        display_board(comp_board)
        print("CURRENT PLAYER BOARD: ", player_ships, "HITS REMAINING")
        display_board(player_board)
        print("IT'S COMPUTER'S TURN")

        # computer turn chooses x and y coordinate against player
        comp_x = random.randint(0, 9)
        comp_y = random.randint(0, 9)

        # this determines if the computer hits the player ship
        comp_hit = (player_board[comp_y][comp_x] == PLAYER_SHIP)

        #  this will let the user know if computer hit player or not
        if(comp_hit):
            print("Your ship was hit!")
            # updates how many hits the player has left 
            player_ships = player_ships - 1

            # if the player lost all hit, the ship location turns into an 'x'
            if(player_ships == 0):
                player_board[comp_y][comp_x] = HIT
            else:
                # moves the player ship to another random location 
                player_board[comp_y][comp_x] = STAR
                new_x = random.choice(list(COLUMN_INDICES))
                new_y = random.randint(0, 9)
                print ('Your new location is at', new_x, new_y, '.')
                print ('Your ship can now take', player_ships, 'hits.')
                new_x = COLUMN_INDICES[new_x]
                player_board[new_y][new_x] = PLAYER_SHIP
                print()

            # end if
            
        else:
            print("Your ship is safe.")
            print ('Your ship can now take', player_ships, 'hits.')
            print()

        # end if
            
        print("CURRENT COMPUTER BOARD: ", comp_ships, "SHIPS REMAINING")
        display_board(comp_board)
        print("CURRENT PLAYER BOARD: ", player_ships, "HITS REMAINING")
        display_board(player_board)

    # returns player_ships
    return player_ships == 0
            
    

# Function display_Board
# Description:
#	This displays the board and peices
# Calls:
#	<names of all functions called, one per line>
# Parameters:
#	None
# Returns:
#	board    2D list

def setup_board():
    
    # declare variables
    row = []
    board = []

    # This sets up the boards
    for number in range (0, MAX_ROW):
        
        row = []

    # end for

        for i in range(MAX_COL):
            row.append(' * ')

        # end for

        # this adds board to the row
        board.append (row)
    return board

# End Function

# Function display_Board
# Description:
#	This displays the board and peices
# Calls:
#	<names of all functions called, one per line>
# Parameters:
#	board   2D list
# Returns:
#	<return value>

def display_board (board):

    # Declare local variables
    number = 0
 
    # board
    print (''.join(COLUMNS))

    for number in range (0, MAX_ROW):
        print (number, ''.join(board[number]))

    # end for   

    # Return values

# End Function

# Function random_ships
# Description:
#	generates random locations to the board
# Calls:
#	<names of all functions called, one per line>
# Parameters:
#	board   2D list
# Returns:
#	ship    Integer

def enemy_ships (board):

    # Declare local variableEs
    ship = 0

    # this places any random ship on the board between 5 - 25
    number_of_ships = random.randint(5, 25)

    # this loops the ships on to the board.
    for ship in range (number_of_ships):
        x = random.randint(0, MAX_COL - 1)
        y = random.randint(0, MAX_ROW - 1)

        # this check if the location has ships
        while board[y][x] == COMPUTER_SHIP:
            
            x = random.randint(0, MAX_COL - 1)
            y = random.randint(0, MAX_ROW - 1)

        # end while

    # end for

        # it places the computer ship on the board
        board[y][x] = COMPUTER_SHIP

    print ('Enemy ships total:', ship + 1)

    # Return ship
    return ship + 1

# End Function


main()
