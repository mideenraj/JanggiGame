# This program is a representation of the board game 'Janggi', or Korean Chess as it is commonly known as.This game can
# be played by two players, allowing them to make alternating moves until one player's general is checkmated. Users
# have the added functionality to check player's turn and also check state of the game at any point during a game.


class JanggiGame:
    """A Class representing the korean chess game, Janggi."""

    def __init__(self):
        """Initializes starting player, game state, board (through nested lists), blue and red player's individual
        fortress coordinates, blue and red's individual pieces."""
        self._player_turn = "BLUE"
        self._game_state = "UNFINISHED"
        #                 0       1       2       3        4        5       6        7       8
        self._board = [["RR1",  "RE1",   "RH1",  "RA1",   None,   "RA2",   "RE2",  "RH2",  "RR2"],  # 0
                       [None,   None,    None,   None,   "RG",    None,    None,    None,   None],  # 1
                       [None,   "RC1",   None,   None,    None,   None,    None,   "RC2",   None],  # 2
                       ["RS1",  None,    "RS2",  None,   "RS3",   None,    "RS4",   None,  "RS5"],  # 3
                       [None,   None,    None,   None,    None,   None,    None,    None,   None],  # 4
                       [None,   None,    None,   None,    None,   None,    None,    None,   None],  # 5
                       ["BS1",  None,   "BS2",   None,   "BS3",   None,    "BS4",   None,  "BS5"],  # 6
                       [None,   "BC1",   None,   None,    None,   None,    None,   "BC2",   None],  # 7
                       [None,   None,    None,   None,    "BG",   None,    None,    None,   None],  # 8
                       ["BR1",  "BE1",  "BH1",   "BA1",   None,   "BA2",   "BE2",   "BH2", "BR2"]]  # 9
        self._blue_fortress = ['73', '74', '75', '83', '84', '85', '93', '94', '95']
        self._red_fortress = ['03', '04', '05', '13', '14', '15', '23', '24', '25']
        self._blue_pieces = ['BG', 'BA1', 'BA2', 'BR1', 'BR2', 'BE1', 'BE2', 'BH1', 'BH2', 'BC1', 'BC2', 'BS1', 'BS2', 'BS3', 'BS4', 'BS5']
        self._red_pieces = ['RG', 'RA1', 'RA2', 'RR1', 'RR2', 'RE1', 'RE2', 'RH1', 'RH2', 'RC1', 'RC2', 'RS1', 'RS2', 'RS3', 'RS4', 'RS5']

    def print_board(self):
        """Prints the board in its current state."""
        print("      A     B     C     D     E     D     G     H     I     ")
        print("    ____________________________________________________")
        for row in range(len(self._board)):
            this_row = f"{row+1}  | "
            for col in self._board[row]:
                if col in ["RG", "BG"]:
                    this_row += col + " "
                elif col:
                    this_row += col
                else:
                    this_row += " - "
                this_row += "   "
            print(this_row)

    def get_game_state(self):
        """Returns the current state of the game."""
        return self._game_state

    def set_game_state(self, state):
        """Sets game state to the inputted state."""
        self._game_state = state

    def get_player_turn(self):
        """Returns the player whose turn it currently is."""
        return self._player_turn

    def set_player_turn(self, player):
        """Sets player turn to the inputted player."""
        self._player_turn = player

    def get_board(self):
        """Returns the board, which is represented by nested lists."""
        return self._board

    def is_in_check(self, player):
        """Takes a player as an argument and returns True if the move made by that respective player has not left
        their general in check. Returns False otherwise"""
        player = player.upper()
        board = self.get_board()
        current_player_turn = self.get_player_turn()     # Stores the player whose turn it is
        checkmate = False

        # Checks if BLUE's general is in check
        if player == "BLUE":
            self.set_player_turn("RED")  # Temporarily sets turn as opposing player's

            # Access position of BLUE general
            blue_general_position = []
            for row in self.get_board():
                if "BG" in row:
                    blue_general_position.append(self.get_board().index(row))
                    blue_general_position.append(row.index("BG"))

            # Checks if any of remaining RED's pieces pose a threat to the general
            for r_piece in self._red_pieces:
                r_piece_location = []
                for row in self.get_board():
                    if r_piece in row:
                        r_piece_location.append(self.get_board().index(row))
                        r_piece_location.append(row.index(r_piece))
                if r_piece != 'RG' or r_piece != 'RA1' or r_piece != 'RA2' and len(r_piece_location) != 0:
                    if board[r_piece_location[0]][r_piece_location[1]][1] == "S" and self.soldier(r_piece_location, blue_general_position) is True:
                        checkmate = True
                        break
                    elif board[r_piece_location[0]][r_piece_location[1]][1] == "R" and self.chariot(r_piece_location, blue_general_position) is True:
                        checkmate = True
                        break
                    elif board[r_piece_location[0]][r_piece_location[1]][1] == "H" and self.horse(r_piece_location, blue_general_position) is True:
                        checkmate = True
                        break
                    elif board[r_piece_location[0]][r_piece_location[1]][1] == "E" and self.elephant(r_piece_location, blue_general_position) is True:
                        checkmate = True
                        break
                    elif board[r_piece_location[0]][r_piece_location[1]][1] == "C" and self.cannon(r_piece_location, blue_general_position) is True:
                        checkmate = True
                        break

        # Checks if RED's general is in check
        if player == "RED":
            self.set_player_turn("BLUE")  # Temporarily sets turn as opposing player's

            # Access position of RED general
            red_general_position = []

            for row in self.get_board():
                if "RG" in row:
                    red_general_position.append(self.get_board().index(row))
                    red_general_position.append(row.index("RG"))

            # Checks if any of remaining BLUE's pieces pose a threat to the general
            for b_piece in self._blue_pieces:
                b_piece_location = []
                for row in self.get_board():
                    if b_piece in row:
                        b_piece_location.append(self.get_board().index(row))
                        b_piece_location.append(row.index(b_piece))
                if b_piece != 'BG' or b_piece != 'BA1' or b_piece != 'BA2':
                    if board[b_piece_location[0]][b_piece_location[1]][1] == "S" and self.soldier(b_piece_location, red_general_position) is True:
                        checkmate = True
                        break
                    elif board[b_piece_location[0]][b_piece_location[1]][1] == "R" and self.chariot(b_piece_location, red_general_position) is True:
                        checkmate = True
                        break
                    elif board[b_piece_location[0]][b_piece_location[1]][1] == "H" and self.horse(b_piece_location, red_general_position) is True:
                        checkmate = True
                        break
                    elif board[b_piece_location[0]][b_piece_location[1]][1] == "E" and self.elephant(b_piece_location, red_general_position) is True:
                        checkmate = True
                        break
                    elif board[b_piece_location[0]][b_piece_location[1]][1] == "C" and self.cannon(b_piece_location, red_general_position) is True:
                        checkmate = True
                        break

        self.set_player_turn(current_player_turn)   # Returns turn to current player.
        if checkmate is True:
            return True         # Returns True if general of specified player is in check
        elif checkmate is False:
            return False        # Returns False if general of specified player is not in check

    def check_if_checkmated(self, player, p_initial):
        """Takes a player as an argument and returns True if the player's general is checkmated with no moves that
        can help it escape. Returns False otherwise. """
        board = self.get_board()                  # Assign variable to to represent board
        current_player = self.get_player_turn()
        self.set_player_turn(player)

        if self.get_player_turn() == player:
            # Access the location of each piece on board
            for each_row in board:  # Iterates through each row (aka sub_list) on board
                for each_element in each_row:  # Iterates through each element in each sub-list
                    if each_element is not None and each_element[0] == p_initial:  # If the square is not empty and the piece belongs to this player
                        piece_location = [board.index(each_row), each_row.index(each_element)]  # Stores the coordinate of the piece within a list

                        # Accesses the location of each square on the board.
                        for each_target_row in board:  # Iterates through each of board, once again.
                            for each_target_column in range(0, len(each_target_row)):  # Iterates through each possible square of the current row
                                if board[board.index(each_target_row)][each_target_column] is None or board[board.index(each_target_row)][each_target_column][0] != p_initial:  # If the destination square is empty or if it does not contain an allied piece (aka it is occupied by an enemy piece)
                                    target_location = [board.index(each_target_row), each_target_column]  # Stores the coordinate of the hypothetical target location

                                    # Check validity of move and store result in variable
                                    if board[piece_location[0]][piece_location[1]][1] == "A" and self.advisor(
                                            piece_location, target_location) is True or \
                                            board[piece_location[0]][piece_location[1]][1] == "G" and self.general(
                                        piece_location, target_location) is True or \
                                            board[piece_location[0]][piece_location[1]][1] == "S" and self.soldier(
                                        piece_location, target_location) is True or \
                                            board[piece_location[0]][piece_location[1]][1] == "R" and self.chariot(
                                        piece_location, target_location) is True or \
                                            board[piece_location[0]][piece_location[1]][1] == "H" and self.horse(
                                        piece_location, target_location) is True or \
                                            board[piece_location[0]][piece_location[1]][1] == "E" and self.elephant(
                                        piece_location, target_location) is True or \
                                            board[piece_location[0]][piece_location[1]][1] == "C" and self.cannon(
                                        piece_location, target_location) is True:
                                        move_validity = True
                                    else:
                                        move_validity = False

                                    # Make the hypothetical move, check general checkmate status, and then reverse move
                                    if move_validity is True:

                                        # ----------------Make move----------------
                                        # Store piece being moved and also piece being captured, if any
                                        piece_being_moved = board[piece_location[0]][piece_location[1]]
                                        possible_piece_being_captured = board[target_location[0]][target_location[1]]

                                        # Move piece to target square and erase from original position
                                        board[target_location[0]][target_location[1]] = piece_being_moved
                                        board[piece_location[0]][piece_location[1]] = None

                                        # Delete captured piece (if any) from list of enemy pieces
                                        if p_initial == "B" and possible_piece_being_captured is not None:
                                            self._red_pieces.remove(possible_piece_being_captured)
                                        elif p_initial == "R" and possible_piece_being_captured is not None:
                                            self._blue_pieces.remove(possible_piece_being_captured)

                                        # ----------------Check general checkmate status----------------
                                        if player == "BLUE":
                                            general_compromised = self.is_in_check("BLUE")
                                        elif player == "RED":
                                            general_compromised = self.is_in_check("RED")

                                        # ----------------Reverse move----------------
                                        # Return piece to original position and delete from position it had been moved to
                                        board[piece_location[0]][piece_location[1]] = piece_being_moved
                                        board[target_location[0]][target_location[1]] = possible_piece_being_captured

                                        # Re-add piece (if any) to enemy piece list
                                        if p_initial == "B" and possible_piece_being_captured is not None:
                                            self._red_pieces.append(possible_piece_being_captured)
                                        elif p_initial == "R" and possible_piece_being_captured is not None:
                                            self._blue_pieces.append(possible_piece_being_captured)

                                    # Returns False if general is not Checkmated
                                    if move_validity is True and general_compromised is False:
                                        self.set_player_turn(current_player)
                                        return False

                                    # ...Otherwise current iteration naturally ends and moves onto the next

        self.set_player_turn(current_player)
        return True  # Return True if general is checkmated (aka none of the returns in this method were triggered)

    def modify_coordinate(self, from_square, to_square):
        """Takes as argument two alphanumerals, representing the current location (where piece currently resides) and
        target location (where piece will be moved to). Both coordinates are decoded to yield 2 separate lists that
        correlate to the particular index on the board, after which they are returned."""

        if from_square[0].lower() == "a":
            from_square[0] = 0
        elif from_square[0].lower() == "b":
            from_square[0] = 1
        elif from_square[0].lower() == "c":
            from_square[0] = 2
        elif from_square[0].lower() == "d":
            from_square[0] = 3
        elif from_square[0].lower() == "e":
            from_square[0] = 4
        elif from_square[0].lower() == "f":
            from_square[0] = 5
        elif from_square[0].lower() == "g":
            from_square[0] = 6
        elif from_square[0].lower() == "h":
            from_square[0] = 7
        elif from_square[0].lower() == "i":
            from_square[0] = 8
        if len(from_square) == 3:
            from_square[1] = 9
        else:
            from_square[1] = int(from_square[1]) - 1

        if to_square[0].lower() == "a":
            to_square[0] = 0
        elif to_square[0].lower() == "b":
            to_square[0] = 1
        elif to_square[0].lower() == "c":
            to_square[0] = 2
        elif to_square[0].lower() == "d":
            to_square[0] = 3
        elif to_square[0].lower() == "e":
            to_square[0] = 4
        elif to_square[0].lower() == "f":
            to_square[0] = 5
        elif to_square[0].lower() == "g":
            to_square[0] = 6
        elif to_square[0].lower() == "h":
            to_square[0] = 7
        elif to_square[0].lower() == "i":
            to_square[0] = 8
        if len(to_square) == 3:
            to_square[1] = 9
        else:
            to_square[1] = int(to_square[1]) - 1
        return from_square, to_square

    def soldier(self, from_square, to_square):
        """Takes as arguments 2 lists representing the current position of the specified 'soldier' game piece and the  target
        location. Returns True if move is valid, otherwise returns False."""

        from_square_str = str(from_square[0]) + str(from_square[1])
        to_square_str = str(to_square[0]) + str(to_square[1])
        blue_fortress_diagonal_move_squares = ['73', '84', '75']
        red_fortress_diagonal_move_squares = ['23', '14', '25']

        # Checks if an orthogonal move is valid (Both within and outside of fortress)
        if from_square_str not in blue_fortress_diagonal_move_squares and from_square_str not in red_fortress_diagonal_move_squares:
            if (self.get_player_turn() == "BLUE") and (from_square[0] - to_square[0] == 1) and (from_square[1] - to_square[1] == 0):
                return True     # Returns True if a valid vertical move is made by BLUE.
            elif (self.get_player_turn() == "RED") and (from_square[0] - to_square[0] == -1) and (from_square[1] - to_square[1] == 0):
                return True     # Returns True if a valid vertical move is made by RED.
            elif (from_square[0] - to_square[0] == 0) and abs((from_square[1] - to_square[1])) == 1:
                return True     # Returns True if a valid horizontal move was made by either BLUE or RED player.

        # Checks if a vertical/horizontal/diagonal move from any of three special RED fortress points is valid.
        if self.get_player_turn() == "BLUE" and from_square_str in red_fortress_diagonal_move_squares:
            if (from_square[0] - to_square[0] == 1) and (from_square[1] - to_square[1] == 0):
                return True    # Returns True if a valid vertical move is made by BLUE from any 1 of 3 fortress points.
            elif (from_square[0] - to_square[0] == 0) and (abs(from_square[1] - to_square[1]) == 1):
                return True    # Returns True if a valid horizontal move is made by BLUE from any 1 of 3 fortress points.
            elif from_square_str == '14':
                if to_square_str == '03' or to_square == '05':
                    return True     # Returns True if a valid diagonal from the the midpoint of RED fortress is made.
            elif from_square_str == '23' or from_square_str == '25':
                if to_square_str == '14':
                    return True     # Returns True if a valid diagonal from either outer two RED fortress entrances is made.

        # Checks if a vertical/horizontal/diagonal move from any of three special BLUE fortress points is valid.
        if self.get_player_turn() == "RED" and from_square_str in blue_fortress_diagonal_move_squares:
            if (from_square[0] - to_square[0] == -1) and (from_square[1] - to_square[1] == 0):
                return True     # Returns True if a valid vertical move is made by RED from any 1 of 3 fortress points.
            elif (from_square[0] - to_square[0] == 0) and (abs(from_square[1] - to_square[1]) == 1):
                return True     # Returns True if a valid horizontal move is made by RED from any 1 of 3 fortress points.
            elif from_square_str == '84':
                if to_square_str == '93' or to_square_str == '95':
                    return True      # Returns True if a valid diagonal from the the midpoint of BLUE fortress is made.
            elif from_square_str == '73' or '75':
                if to_square_str == '84':
                    return True  # Returns True if a valid diagonal from either outer two BLUE fortress entrances is made.

        # Returns False if move is invalid
        return False

    def general(self, from_square, to_square):
        """Takes as arguments 2 lists representing the current position of the 'general' game piece and the target
            location. Returns True if move is valid, otherwise returns False."""
        from_square_str = str(from_square[0]) + str(from_square[1])
        to_square_str = str(to_square[0]) + str(to_square[1])
        blue_fortress_corners = ['73', '75', '93', '95']
        red_fortress_corners = ['03', '05', '23', '25']

        # If BLUE player is making a move
        if self.get_player_turn() == "BLUE":
            if to_square_str not in self._blue_fortress:
                return False        # If a move to outside of BLUE fortress is made
            if (abs(from_square[0] - to_square[0]) == 1) and (from_square[1] - to_square[1] == 0):
                return True         # If a valid vertical move is made.
            elif (from_square[0] - to_square[0] == 0) and (abs(from_square[1] - to_square[1]) == 1):
                return True         # If a valid horizontal move is made
            elif from_square_str in blue_fortress_corners:
                if to_square_str == '84':
                    return True     # If a move from one of the 4 corner to midpoint is made.
            elif from_square_str == '84':
                if to_square_str in blue_fortress_corners:
                    return True      # If a move from the fortress midpoint to one of the 4 corners is made.

        # If RED player if making a move
        if self.get_player_turn() == "RED":
            if to_square_str not in self._red_fortress:
                return False        # If a move to outside of RED fortress is made
            elif (abs(from_square[0] - to_square[0]) == 1) and (from_square[1] - to_square[1] == 0):
                return True          # If a valid vertical move is made.
            elif (from_square[0] - to_square[0] == 0) and (abs(from_square[1] - to_square[1]) == 1):
                return True         # If a valid horizontal move is made
            elif from_square_str in red_fortress_corners:
                if to_square_str == '14':
                    return True     # If a move from one of the 4 corner to midpoint is made.
            elif from_square_str == '14':
                if to_square_str in red_fortress_corners:
                    return True      # If a move from the fortress midpoint to one of the 4 corners is made.

        # Returns False if move is invalid
        return False

    def advisor(self, from_square, to_square):
        """Takes as arguments 2 lists representing the current position of the specified 'advisor' game piece and the
        target location. Returns True if move is valid, otherwise returns False."""
        from_square_str = str(from_square[0]) + str(from_square[1])
        to_square_str = str(to_square[0]) + str(to_square[1])
        blue_fortress_corners = ['73', '75', '93', '95']
        red_fortress_corners = ['03', '05', '23', '25']

        # If BLUE player is making a move
        if self.get_player_turn() == "BLUE":
            if to_square_str not in self._blue_fortress:
                return False        # If a move to outside of BLUE fortress is made
            if (abs(from_square[0] - to_square[0]) == 1) and (from_square[1] - to_square[1] == 0):
                return True         # If a valid vertical move is made.
            elif (from_square[0] - to_square[0] == 0) and (abs(from_square[1] - to_square[1]) == 1):
                return True         # If a valid horizontal move is made
            elif from_square_str in blue_fortress_corners:
                if to_square_str == '84':
                    return True     # If a move from one of the 4 corner to midpoint is made.
            elif from_square_str == '84':
                if to_square_str in blue_fortress_corners:
                    return True      # If a move from the fortress midpoint to one of the 4 corners is made.

        # If RED player if making a move
        if self.get_player_turn() == "RED":
            if to_square_str not in self._red_fortress:
                return False        # If a move to outside of RED fortress is made
            elif (abs(from_square[0] - to_square[0]) == 1) and (from_square[1] - to_square[1] == 0):
                return True          # If a valid vertical move is made.
            elif (from_square[0] - to_square[0] == 0) and (abs(from_square[1] - to_square[1]) == 1):
                return True         # If a valid horizontal move is made
            elif from_square_str in red_fortress_corners:
                if to_square_str == '14':
                    return True     # If a move from one of the 4 corner to midpoint is made.
            elif from_square_str == '14':
                if to_square_str in red_fortress_corners:
                    return True      # If a move from the fortress midpoint to one of the 4 corners is made.

        # Returns False if move is invalid
        return False

    def chariot(self, from_square, to_square):
        """Takes as arguments 2 lists representing the current position of the specified 'chariot' game piece and the
        target location. Returns True if move is valid, otherwise returns False."""
        diagonal_move_positions = ['14', '03', '05', '23', '25', '84', '73', '75', '93', '95']
        blue_fortress_corners = ['73', '75', '93', '95']
        red_fortress_corners = ['03', '05', '23', '25']
        restricted_moves_from_fortress_top_middle = ['13', '15', '23', '25', '83', '85', '93', '95']
        restricted_moves_from_fortress_bottom_middle = ['03', '05', '13', '15', '73', '75', '83', '85']
        restricted_moves_from_fortress_left_middle = ['04', '05', '24', '25', '74', '75', '94', '95']
        restricted_moves_from_fortress_right_middle = ['03', '04', '23', '24', '73', '74', '93', '94']
        from_square_str = str(from_square[0]) + str(from_square[1])
        to_square_str = str(to_square[0]) + str(to_square[1])

        # If move is orthogonal
        if (from_square[0] - to_square[0] == 0 and abs(from_square[1] - to_square[1]) > 0) or (abs(from_square[0] - to_square[0]) > 0 and from_square[1] - to_square[1] == 0):
            # If a Vertical move is being made from blue side of board to red side.
            if (from_square[1] - to_square[1] == 0) and (from_square[0] - to_square[0] > 0):
                for square in range(from_square[0]-1, to_square[0], -1):    # Checks each square between from and to square for a piece.
                    if self.get_board()[square][from_square[1]] is not None:
                        return False   # Returns False if the chariot traverses over another piece (allied or enemy) on its way to the destination square.
            # If a Vertical move is being made from red side of board to blue side.
            if (from_square[1] - to_square[1] == 0) and (from_square[0] - to_square[0] < 0):
                for square_1 in range(from_square[0]+1, to_square[0]):
                    if self.get_board()[square_1][from_square[1]] is not None:
                        return False   # Returns False if the chariot traverses over another piece (allied or enemy) on its way to the destination square.
            # If a Horizontal move is being made from left side of board to right side.
            if (from_square[0] - to_square[0] == 0) and (from_square[1] - to_square[1] < 0):
                for square_2 in range(from_square[1]+1, to_square[1]):
                    if self.get_board()[from_square[0]][square_2] is not None:
                        return False   # Returns False if the chariot traverses over another piece (allied or enemy) on its way to the destination square.
            # If a Horizontal move is being made from right side of board to left side.
            if (from_square[0] - to_square[0] == 0) and (from_square[1] - to_square[1] > 0):
                for square_3 in range(from_square[1]-1, to_square[1], -1):
                    if self.get_board()[from_square[0]][square_3] is not None:
                        return False   # Returns False if the chariot traverses over another piece (allied or enemy) on its way to the destination square.
            return True     # Returns True if a valid orthogonal move is made.

        # Checks moves that start from the corner or midpoint of either fortress
        if from_square_str in diagonal_move_positions:
            bfm = '84'  # Blue Fortress Midpoint
            rfm = '14'  # Red Fortress Midpoint

            # General check
            if from_square_str == bfm and to_square_str not in blue_fortress_corners:
                return False    # Returns False if an invalid diagonal move from BLUE fortress midpoint was made.
            elif from_square == rfm and to_square_str not in red_fortress_corners:
                return False    # Returns False if an invalid diagonal move from RED fortress midpoint was made.
            elif from_square_str in blue_fortress_corners and to_square_str not in self._blue_fortress:
                return False    # Returns False if an invalid move from any of the BLUE fortress corner's is made
            elif from_square_str in red_fortress_corners and to_square_str not in self._red_fortress:
                return False    # Returns False if an invalid move from any of the RED fortress corner's is made
            elif from_square_str in blue_fortress_corners and to_square_str in blue_fortress_corners and self.get_board()[int(bfm[0])][int(bfm[1])] is not None:
                return False    # Returns False if a jump is made over the BLUE fortress midpoint while its occupied.
            elif from_square_str in red_fortress_corners and to_square_str in red_fortress_corners and self.get_board()[int(rfm[0])][int(rfm[1])] is not None:
                return False    # Returns False if a jump is made over the RED fortress midpoint while its occupied.

            # If an invalid move is made from any of the 4 corners of wither fortress to another illegal part of the fortress
            elif (from_square_str == '25' or from_square == '95') and (to_square_str == str(from_square[0]-1)+str(from_square[1]-2) or to_square_str == str(from_square[0]-2)+str(from_square[1]-1)):
                return False    # Returns False if a move is made from the lower right corner of either fortress to fortress middle left or top middle.
            elif (from_square_str == '23' or from_square == '93') and (to_square_str == str(from_square[0]-1)+str(from_square[1]+2) or to_square_str == str(from_square[0]-2)+str(from_square[1]+1)):
                return False    # Returns False if a move is made from the lower left corner of either fortress to fortress top middle or middle right.
            elif (from_square_str == '73' or from_square == '03') and (to_square_str == str(from_square[0]+1)+str(from_square[1]+2) or to_square_str == str(from_square[0]+2)+str(from_square[1]+1)):
                return False    # Returns False if a move is made from the rop right corner of either fortress to fortress middle right or bottom middle.
            elif (from_square_str == '05' or from_square == '75') and (to_square_str == str(from_square[0]+1)+str(from_square[1]-2) or to_square_str == str(from_square[0]+2)+str(from_square[1]-1)):
                return False    # Returns False if a move is made from the top right corner of either fortress to fortress bottom middle or middle left.

            # If an invalid move is made from any of the 4 sides (not corners) of either fortress to another part of that fortress
            elif from_square_str == '04' or from_square_str == '74' and to_square_str in restricted_moves_from_fortress_top_middle:
                return False
            elif from_square_str == '24' or from_square_str == '94' and to_square_str in restricted_moves_from_fortress_bottom_middle:
                return False
            elif from_square_str == '13' or from_square_str == '83' and to_square_str in restricted_moves_from_fortress_left_middle:
                return False
            elif from_square_str == '15' or from_square_str == '85' and to_square_str in restricted_moves_from_fortress_right_middle:
                return False

            return True     # Returns True if a valid move from fortress is made.

        return False    # Returns False is an invalid move is made

    def horse(self, from_square, to_square):
        """Takes as arguments 2 lists representing the current position of the specified 'horse' game piece and the
        target location. Returns True if move is valid, otherwise returns False."""

        # Vertical move
        if (abs(from_square[0] - to_square[0]) ==  2) and (abs(from_square[1] - to_square[1]) == 1):
            if from_square[0] - to_square[0] > 0 and self.get_board()[from_square[0]-1][from_square[1]] is None:
                return True     # If a valid move is made towards RED side and path is not obstructed by another piece
            elif from_square[0] - to_square[0] < 0 and self.get_board()[from_square[0]+1][from_square[1]] is None:
                return True     # If a valid move is made towards BLUE side and path is not obstructed by another piece

        # Horizontal move
        if (abs(from_square[0] - to_square[0]) == 1) and (abs(from_square[1] - to_square[1]) == 2):
            if from_square[1] - to_square[1] > 0 and self.get_board()[from_square[0]][from_square[1]-1] is None:
                return True     # If a valid horizontal to the left was made and path is not obstructed by another piece
            elif from_square[1] - to_square[1] < 0 and self.get_board()[from_square[0]][from_square[1]+1] is None:
                return True     # If a valid horizontal to the right was made and path is not obstructed by another piece

        return False       # Returns False if an invalid move was made

    def elephant(self, from_square, to_square):
        """Takes as arguments 2 lists representing the current position of the specified 'elephant' game piece and the
        target location. Returns True if move is valid, otherwise returns False."""

        # Vertical Move
        if abs(from_square[0] - to_square[0]) == 3 and abs(from_square[1] - to_square[1]) == 2:

            # If the move is made towards RED's side and the first encountered square in the move path is unoccupied
            if from_square[0] - to_square[0] > 0 and self.get_board()[from_square[0]-1][from_square[1]] is None:

                # If the diagonal part of the move is to the right and if the second square in the path move is unoccupied
                if from_square[1] - to_square[1] < 0 and self.get_board()[from_square[0]-2][from_square[1]+1] is None:
                    return True

                # If the diagonal part of the move is to the left and if the second square in the move path is unoccupied
                elif from_square[1] - to_square[1] > 1 and self.get_board()[from_square[0]-2][from_square[1]-1] is None:
                    return True

            # If the move is made towards BLUE's side and the first encountered square in the move path is unoccupied
            if from_square[0] - to_square[0] < 0 and self.get_board()[from_square[0]+1][from_square[1]] is None:

                # If the diagonal part of the move is to the right and if the second square in the path move is unoccupied
                if from_square[1] - to_square[1] < 0 and self.get_board()[from_square[0]+2][from_square[1]+1] is None:
                    return True

                # If the diagonal part of the move is to the left and if the second square in the path move is unoccupied
                elif from_square[1] - to_square[1] > 0 and self.get_board()[from_square[0]+2][from_square[1]-1] is None:
                    return True

        # Horizontal Move
        if abs(from_square[0] - to_square[0]) == 2 and abs(from_square[1] - to_square[1]) == 3:

            # If the move is made towards the left of the board and the first encountered square in the move path is unoccupied
            if from_square[0] - to_square[0] > 0 and self.get_board()[from_square[0]][from_square[1]-1] is None:

                # If the diagonal part of the move is towards RED's side of the board and the second square in the math is unoccupied
                if from_square[0] - to_square[0] > 0 and self.get_board()[from_square[0]-1][from_square[1]-2] is None:
                    return True

                # If the diagonal part of the move is towards BLUE's side of the board and the second square in the math is unoccupied
                if from_square[0] - to_square[0] < 0 and self.get_board()[from_square[0]+1][from_square[1]-2] is None:
                    return True

            # If the move is made towards the right of the board and the first encountered square in the move path is unoccupied
            if from_square[0] - to_square[1] < 0 and self.get_board()[from_square[0]][from_square[1]+1] is None:

                # If the diagonal part of the move is towards RED's side of the board and the second square in the math is unoccupied
                if from_square[0] - to_square[0] > 0 and self.get_board()[from_square[0]-1][from_square[1]+2] is None:
                    return True

                # If the diagonal part of the move is towards BLUE's side of the board and the second square in the math is unoccupied
                if from_square[0] - to_square[0] > 0 and self.get_board()[from_square[0]+1][from_square[1]+1] is None:
                    return None

        return False    # Returns False if move is invalid

    def cannon(self, from_square, to_square):
        """Takes as arguments 2 lists representing the current position of the specified 'cannon' game piece and the
        target location. Returns True if move is valid, otherwise returns False."""

        blue_fortress_corners = ['73', '75', '93', '95']
        red_fortress_corners = ['03', '05', '23', '25']
        from_square_str = str(from_square[0]) + str(from_square[1])
        to_square_str = str(to_square[0]) + str(to_square[1])
        bfm = '84'
        rfm = '14'

        if self.get_board()[to_square[0]][to_square[1]] is not None and self.get_board()[to_square[0]][to_square[1]][1] == "C":
            return False    # Returns False if piece being captured is another cannon

        # If move is orthogonal
        if ((abs(from_square[0] - to_square[0]) > 0) and (from_square[1] - to_square[1] == 0)) or ((from_square[0] - to_square[0] == 0) and (abs(from_square[1] - to_square[1]) > 1)):

            # If a vertical move is being made from BLUE side of board towards RED side.
            if from_square[0] - to_square[0] > 0 and from_square[1] - to_square[1] == 0:
                number_of_pieces_in_path = 0    # Tracks the # of pieces between current and target square.
                another_canon_in_path = False   # Used to check if another cannon is being jumped over
                for square in range(from_square[0]-1, to_square[0], -1):    # Checks every square between 'from' and 'to' square.
                    if self.get_board()[square][from_square[1]] is not None:
                        number_of_pieces_in_path += 1   # Increments counter for every piece in move route.
                    if self.get_board()[square][from_square[1]] is not None and self.get_board()[square][from_square[1]][1] == "C":
                        another_canon_in_path = True    # Set True if another cannon (allied or enemy) in encountered in move path.
                if number_of_pieces_in_path == 1 and another_canon_in_path is False:
                    return True

            # If a vertical move is being made from RED side of board towards BLUE side.
            if from_square[0] - to_square[0] < 0 and from_square[1] - to_square[1] == 0:
                number_of_pieces_in_path_1 = 0    # Tracks the # of pieces between current and target square.
                another_canon_in_path_1 = False   # Used to check if another cannon is being jumped over
                for square_1 in range(from_square[0]+1, to_square[0]):    # Checks every square between 'from' and 'to' square.
                    if self.get_board()[square_1][from_square[1]] is not None:
                        number_of_pieces_in_path_1 += 1   # Increments counter for every piece in move route.
                    if self.get_board()[square_1][from_square[1]] is not None and self.get_board()[square_1][from_square[1]][1] == "C":
                        another_canon_in_path_1 = True    # Set True if another cannon (allied or enemy) in encountered in move path.
                if number_of_pieces_in_path_1 == 1 and another_canon_in_path_1 is False:
                    return True

            # If a horizontal move is being made from left side of board to right side.
            if from_square[0] - to_square[0] == 0 and from_square[1] - to_square[1] < 0:
                number_of_pieces_in_path_2 = 0    # Tracks the # of pieces between current and target square.
                another_canon_in_path_2 = False   # Used to check if another cannon is being jumped over
                for square_2 in range(from_square[1]+1, to_square[1]):
                    if self.get_board()[from_square[0]][square_2] is not None:
                        number_of_pieces_in_path_2 += 1
                    if self.get_board()[from_square[0]][square_2] is not None and self.get_board()[from_square[0]][square_2][1] == "C":
                        another_canon_in_path_2 = True
                if number_of_pieces_in_path_2 == 1 and another_canon_in_path_2 is False:
                    return True

            # If a horizontal move is being made from right side of board to left side.
            if from_square[0] - to_square[0] == 0 and from_square[1] - to_square[1] > 0:
                number_of_pieces_in_path_3 = 0    # Tracks the # of pieces between current and target square.
                another_canon_in_path_3 = False   # Used to check if another cannon is being jumped over
                for square_3 in range(from_square[1]-1, to_square[1], -1):
                    if self.get_board()[from_square[0]][square_3] is not None:
                        number_of_pieces_in_path_3 += 1
                    if self.get_board()[from_square[0]][square_3] is not None and self.get_board()[from_square[0]][square_3][1] == "C":
                        another_canon_in_path_3 = True
                if number_of_pieces_in_path_3 == 1 and another_canon_in_path_3 is False:
                    return True

        # Checks diagonal moves (Specifically from the corners of each fortress)
        if from_square_str in blue_fortress_corners and to_square_str in blue_fortress_corners:
            if self.get_board()[int(bfm[0])][int(bfm[1])] is not None and self.get_board()[int(bfm[0])][int(bfm[1])][1] != "C":
                return True     # Returns True if a diagonal move from one corner to another is made within the blue fortress with a non-canon piece in the middle
        elif from_square_str in red_fortress_corners and to_square_str in red_fortress_corners:
            if self.get_board()[int(rfm[0])][int(rfm[1])] is not None and self.get_board()[int(rfm[0])][int(rfm[1])][1] != "C":
                return True     # Returns True if a diagonal move from one corner to another is made within the red fortress with a non-canon piece in the middle

        return False    # Returns False if an invalid move was made

    def blue_makes_a_move(self, from_square, to_square):
        """Assisting function that is called by the make_move method when the BLUE player makes a move. Takes as arguments
        two lists that represent the location a piece is being moved from and location being moved to. This function in turn
        calls the method of the appropriate piece being moved. Returns True if move is valid, otherwise returns False. """

        board = self.get_board()

        if from_square == to_square and self.is_in_check("BLUE") is False:    # If player passes their turn
            self.set_player_turn("RED")
            return True

        # Check if an allied piece is already occupying the target square
        if board[to_square[0]][to_square[1]] is not None and self.get_board()[to_square[0]][to_square[1]][0] == "B":
            return False

        # Check is piece_specific move is valid
        if board[from_square[0]][from_square[1]][1] == "S":    # If piece being moved is the Soldier
            move_status = self.soldier(from_square, to_square)
        elif board[from_square[0]][from_square[1]][1] == "G":    # If piece being moved is the General
            move_status = self.general(from_square, to_square)
        elif board[from_square[0]][from_square[1]][1] == "A":    # If piece being moved is the Advisor
            move_status = self.advisor(from_square, to_square)
        elif board[from_square[0]][from_square[1]][1] == "R":    # If piece being moved is the Chariot
            move_status = self.chariot(from_square, to_square)
        elif board[from_square[0]][from_square[1]][1] == "H":    # If piece being moved is the Horse
            move_status = self.horse(from_square, to_square)
        elif board[from_square[0]][from_square[1]][1] == "E":    # If piece being moved is the Elephant
            move_status = self.elephant(from_square, to_square)
        elif board[from_square[0]][from_square[1]][1] == "C":    # If piece being moved is the Cannon
            move_status = self.cannon(from_square, to_square)

        if move_status is False:
            return False

        # If move is valid, make the move and call is_in_check
        if move_status is True:
            piece_being_moved = self.get_board()[from_square[0]][from_square[1]]    # Stores piece being moved
            piece_being_captured = self.get_board()[to_square[0]][to_square[1]]     # Stores piece being captured (if any)

            # Checks if a piece was captured, if so, it is removed from list of RED's pieces
            if piece_being_captured is not None:
                self._red_pieces.remove(piece_being_captured)

            # Removes piece from current location
            self.get_board()[from_square[0]][from_square[1]] = None

            # Moves piece to destination
            self.get_board()[to_square[0]][to_square[1]] = piece_being_moved

            # Calls is_in_check to check if move caused general to be in check
            general_in_check = self.is_in_check("BLUE")

        # If move was valid but move has put general in check: move is undone and False is returned
        if move_status is True and general_in_check is True:

            # Moving piece is moved back into its original position
            self.get_board()[from_square[0]][from_square[1]] = piece_being_moved

            # If an enemy piece was captured in the move: it is replaced to its original position and the captured piece
            #  is re-added to list of red pieces. Otherwise: NONE is initialized to moved position. Finally Returns False.
            if piece_being_captured is not None:
                self.get_board()[to_square[0]][to_square[1]] = piece_being_captured
                self._red_pieces.append(piece_being_captured)
            else:
                self.get_board()[to_square[0]][to_square[1]] = None
            return False

        # If move was valid and move did not put general in check
        if move_status is True and general_in_check is False:
            self.set_player_turn("RED")
            return True

    def red_makes_a_move(self, from_square, to_square):
        """Helper function that is called by the make_move method when the RED player makes a move. Takes as arguments
        two lists that represent the location a piece is being moved from and location being moved to. This function in turn
        calls the method of the appropriate piece being moved. Returns True if move is valid, otherwise returns False. """
        board = self.get_board()

        if from_square == to_square and self.is_in_check("RED") is False:    # If player passes their turn
            self.set_player_turn("BLUE")
            return True

        # Check if an allied piece is already occupying the target square
        if board[to_square[0]][to_square[1]] is not None and self.get_board()[to_square[0]][to_square[1]][0] == "R":
            return False

        # Check is piece_specific move is valid
        elif board[from_square[0]][from_square[1]][1] == "S":    # If piece being moved is the Soldier
            move_status = self.soldier(from_square, to_square)
        elif board[from_square[0]][from_square[1]][1] == "G":    # If piece being moved is the General
            move_status = self.general(from_square, to_square)
        elif board[from_square[0]][from_square[1]][1] == "A":    # If piece being moved is the Advisor
            move_status = self.advisor(from_square, to_square)
        elif board[from_square[0]][from_square[1]][1] == "R":    # If piece being moved is the Chariot
            move_status = self.chariot(from_square, to_square)
        elif board[from_square[0]][from_square[1]][1] == "H":    # If piece being moved is the Horse
            move_status = self.horse(from_square, to_square)
        elif board[from_square[0]][from_square[1]][1] == "E":    # If piece being moved is the Elephant
            move_status = self.elephant(from_square, to_square)
        elif board[from_square[0]][from_square[1]][1] == "C":    # If piece being moved is the Cannon
            move_status = self.cannon(from_square, to_square)

        if move_status is False:
            return False

        # If move is valid, make the move and call is_in_check
        if move_status is True:
            piece_being_moved = self.get_board()[from_square[0]][from_square[1]]    # Stores piece being moved
            piece_being_captured = self.get_board()[to_square[0]][to_square[1]]     # Stores piece being captured (if any)

            # Checks if a piece was captured, if so, it is removed from list of BLUE's pieces
            if piece_being_captured is not None:
                self._blue_pieces.remove(piece_being_captured)

            # Removes piece from current location
            self.get_board()[from_square[0]][from_square[1]] = None

            # Moves piece to destination
            self.get_board()[to_square[0]][to_square[1]] = piece_being_moved

            # Calls is_in_check to check if move caused general to be in check
            general_in_check = self.is_in_check("RED")


        # If move was valid but move has put general in check: move is undone and False is returned
        if move_status is True and general_in_check is True:

            # Moving piece is moved back into its original position
            self.get_board()[from_square[0]][from_square[1]] = piece_being_moved

            # If an enemy piece was captured in the move: it is replaced to its original position and the captured piece
            #  is re-added to list of red pieces. Otherwise: NONE is initialized to moved position. Finally Returns False.
            if piece_being_captured is not None:
                self.get_board()[to_square[0]][to_square[1]] = piece_being_captured
                self._red_pieces.append(piece_being_captured)
            else:
                self.get_board()[to_square[0]][to_square[1]] = None

            return False

        # If move was valid and move did not put general in check: updates player turn and returns True
        if move_status is True and general_in_check is False:
            self.set_player_turn("BLUE")
            return True

    def make_move(self, from_square, to_square):
        """Takes as arguments two alphanumerals, one representing the location a piece is being moved from and the other
        being the location the piece is being moved to. Returns True if move was valid, otherwise returns False."""

    # Decodes 'from' & 'to' inputs (by calling modify_coordinate) to represent indexes on list-represented board.
        from_square_as_list = ["" + fs for fs in from_square]
        to_square_as_list = ["" + ts for ts in to_square]
        self.modify_coordinate(from_square_as_list, to_square_as_list)
        from_square = [int(from_square_as_list[1]), int(from_square_as_list[0])]
        to_square = [int(to_square_as_list[1]), int(to_square_as_list[0])]

    # General input validation (Safety net)
        board = self.get_board()
        if board[from_square[0]][from_square[1]] is None:
            return False              # Returns false if 'from' square is empty
        if self.get_game_state() != "UNFINISHED":
            return False              # Returns False if game has already been won
        if self.get_player_turn() == "BLUE" and board[from_square[0]][from_square[1]][0] == "R":
            return False              # Returns False if BLUE player tries to move RED player piece
        if self.get_player_turn() == "RED" and board[from_square[0]][from_square[1]][0] == "B":
            return False              # Returns False if RED player tries to move BLUE player piece
        if from_square[0] > 9 or from_square[1] > 8 or to_square[0] > 9 or to_square[1] > 8:
            return False              # Returns False if 'from'/'to' inputs exceed length of board in either dimension.
        if from_square[0] < 0 or from_square[1] < 0 or to_square[1] < 0 or to_square[1] < 0:
            return False              # Returns False if 'from'/'to' values is less than 0

        if self.get_player_turn() == "BLUE":
            move_status = self.blue_makes_a_move(from_square, to_square)
            if move_status is False:
                return False
            elif move_status is True:
                if self.check_if_checkmated("RED", "R") is True:
                    self.set_game_state("BLUE_WON")
                    return True
                else:
                    return True

        if self.get_player_turn() == "RED":

            move_status = self.red_makes_a_move(from_square, to_square)
            if move_status is False:
                return False
            elif move_status is True:
                if self.check_if_checkmated("BLUE", "B") is True:
                    self.set_game_state("RED_WON")
                    return True
                else:
                    return True


def main():
    """Driver code for the JanggiGame class."""

    game = JanggiGame()

    # -----To play game turn-by-turn:
    while game.get_game_state() == "UNFINISHED":
        print("\n")
        if game.get_player_turn() == "BLUE":
            game.print_board()
            from_coor = input("BLUE, enter source coordinate: ", )
            to_coor = input("BLUE, enter destination coordinate: ", )
            while game.make_move(from_coor, to_coor) is False:
                print("Invalid input. Please try again!")
                from_coor = input("BLUE, enter source coordinate: ", )
                to_coor = input("BLUE, enter destination coordinate: ", )

        if game.get_player_turn() == "RED":
            print("\n")
            game.print_board()
            from_coor = input("RED, enter source coordinate: ", )
            to_coor = input("RED, enter destination coordinate: ", )
            while game.make_move(from_coor, to_coor) is False:
                print("Invalid input. Please try again!")
                from_coor = input("RED, enter source coordinate: ", )
                to_coor = input("RED, enter destination coordinate: ", )

    # When game is completed...
    print("BLUE wins!" if game.get_game_state() == "BLUE_WON" else "RED wins!")


if __name__ == '__main__':
    main()
