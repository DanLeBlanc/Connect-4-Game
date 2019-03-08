from connect_four_module import *

# initialize Players

player1 = Player('[ X ]')

player2 = Player('[ O ]')

# asks user if they'd like to play the game, after a win or tie asks them again
while True:

    play_game = input("Would you like to play connect 4? y/n ")

    if play_game.lower() == 'y':

        # turn counter, if full draws a tie
        counter = 0

        # asks user for the size of board, between 4 and 10 spots
        while True:

            try:
                board_size = int(input("What size would you like the board? (between 4 and 10): "))
            except:
                print("That is not a number.")
                continue

            if board_size < 4:
                print("Board size too small.")
                continue
            elif board_size > 10:
                print("Board size too big.")
                continue
            else:
                board = Board(board_size)
                break

        # prints initial board
        board.print_board()


        # plays the game
        # takes turn from each player, each turn checks all possible win conditions based
        # on last placed piece
        while True:

            position = board.add_piece(player1.__str__())

            print('\n'*100)

            board.print_board()

            if board.check_win_horizontal(player1,position) or board.check_win_vertical(player1,position)\
            or board.check_win_diagonal(player1,position):
                print("Player 1 wins!")
                break

            counter+=1

            if counter >= board.size**2:
                print("It's a tie!")
                break

            position = board.add_piece(player2.__str__())

            print('\n'*100)

            board.print_board()

            if board.check_win_horizontal(player2,position) or board.check_win_vertical(player2,position)\
            or board.check_win_diagonal(player2,position):
                print("Player 2 wins!")
                break

            counter+=1

            # tie
            if counter >= board.size**2:
                print("It's a tie!")
                break

    # user chose not to play the game, exits
    elif play_game.lower() == 'n':
        print("See ya!")
        break

    # non acceptable income for y/n
    else:
        print("Not an acceptable input.")
        continue