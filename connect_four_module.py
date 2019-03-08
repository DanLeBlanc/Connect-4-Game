class Board():
    """
    Creates a board object to play the game given a user inputed size.
    Contains print_board() method to print the board.
    Contains add_piece() which takes player argument to place a piece.
    Contains win checking functions.
    """
    def __init__(self, size):
        self.size = size
        self.board_list = [['[   ]' for square in range(self.size)] for square in range(self.size)]
    
    # prints board given board size argument
    def print_board(self):
        board_list = self.board_list
        for row in range(self.size):
            print(''.join(board_list[row]) + '\n')

    # adds piece, X or O based on player
    def add_piece(self,player):
        # receives horizontal input
        while True:
            try:
                player_choice = int(input("Where would you like to place a piece? "))
                if player_choice < 1 or player_choice > self.size:
                    print("That is not a place on the board.")
                    continue
                break
            except:
                print("That is not a a valid input.")
                exit()
                continue
        # checks to see if bottom most square is filled, if so places it on top
        # range(len(self.board_list)-1,-1-,1) counts backwards from end of list
        while True:
            for move in range(len(self.board_list)-1,-1,-1):
                if self.board_list[move][player_choice-1] == '[   ]':
                    self.board_list[move][player_choice-1] = player
                    break
            break

        return (move,player_choice-1)

    # horizontal win condition
    def check_win_horizontal(self,player,position):

        # counts number of same pieces in a row
        piece_counter = 0

        # loops through spaces left and right of input, if there are 4 pieces in a row, triggers a win
        try:
            for x in range(4):
                if self.board_list[position[0]][position[1]-x] == player.__str__():
                    piece_counter+=1
                else:
                    break
        except:
            pass

        try:
            for x in range(1,4):
                if self.board_list[position[0]][position[1]+x] == player.__str__():
                    piece_counter+=1
                else:
                    break
        except:
            pass

        return piece_counter >= 4


    # vertical win condition
    def check_win_vertical(self,player,position):

        # if the y coordinate is at least 4 from the bottom, will check to see if
        # there are 3 identical pieces underneath it, triggering a win
        def get_set():
            value_list = []
            if position[0]<self.size-3:
                for y in range(position[0],position[0]+4):
                    value_list.append(self.board_list[y][position[1]])
            return set(value_list)


        if position[0] < self.size-3:
            return get_set() == {str(player)}


    # diagonal win condition
    def check_win_diagonal(self,player,position):


        # loops through pieces to the up right and down left of last place piece,
        # if 4 in a row triggers a win
        def check_up_right_diagonal():

            piece_counter = 0

            try:
                for x in range(4):
                    if self.board_list[position[0]-x][position[1]+x] == player.__str__():
                        piece_counter+=1
                    else:
                        break
            except:
                pass

            try:
                for x in range(1,4):
                    if self.board_list[position[0]+x][position[1]-x] == player.__str__():
                        piece_counter+=1
                    else:
                        break
            except:
                pass

            return piece_counter >= 4


        # loops through pieces to the up left and down right of last placed piece,
        # if 4 in a row triggers a win
        def check_up_left_diagonal():

            piece_counter = 0

            try:
                for x in range(4):
                    if self.board_list[position[0]-x][position[1]-x] == player.__str__():
                        piece_counter+=1
                    else:
                        break
            except:
                pass

            try:
                for x in range(1,4):
                    if self.board_list[position[0]+x][position[1]+x] == player.__str__():
                        piece_counter+=1
                    else:
                        break
            except:
                pass

            return piece_counter >= 4

        return check_up_right_diagonal() or check_up_left_diagonal()
        

# player class, takes argument '[ X ]' or '[ O ]' to create a player

class Player():

    def __init__(self,piece):
        self.piece = piece

    def __str__(self):
        return self.piece