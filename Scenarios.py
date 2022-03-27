
# This script consists of two functions containing method calls to the JanggiGame class that results in BLUE winning.
# This is simply for testing purposes and to gain a better understanding of how the game operates.

from JanggiGame import JanggiGame


def scenario_1():
    """Running this function will result in a series of inputs to the JanggiGame class that results
    in the BLUE player winning the match."""

    game = JanggiGame()
    print("Red in check:", game.is_in_check('red'))
    print("Blue in check:", game.is_in_check('blue'))
    print("1:", game.make_move('a7', 'b7'))
    print("2:", game.make_move('i4', 'h4'))
    print("3:", game.make_move('h10', 'g8'))  # Blue
    print("4:", game.make_move('c1', 'd3'))
    print("5:", game.make_move('h8', 'e8'))
    print("6:", game.make_move('i1', 'i2'))
    print("7:", game.make_move('e7', 'f7'))
    print("Red in check:", game.is_in_check('red'))
    print("Blue in check:", game.is_in_check('blue'))
    print("8:", game.make_move('b3', 'e3'))
    print("Red in check:", game.is_in_check('red'))
    print("Blue in check:", game.is_in_check('blue'))
    print("9:", game.make_move('g10', 'e7'))
    print("10:", game.make_move('e4', 'd4'))
    print("11:", game.make_move('c10', 'd8'))
    print("12:", game.make_move('g1', 'e4'))
    print("13:", game.make_move('f10', 'f9'))  # Blue
    print("14:", game.make_move('h1', 'g3'))
    print("15:", game.make_move('a10', 'a6'))
    print("16:", game.make_move('d4', 'd5'))
    print("17:", game.make_move('e9', 'f10'))  # Blue
    print("18:", game.make_move('h3', 'f3'))
    print("19:", game.make_move('e8', 'h8'))
    print("20:", game.make_move('i2', 'h2'))
    print("21:", game.make_move('h8', 'f8'))  # Blue
    print("22:", game.make_move('f1', 'f2'))
    print("23:", game.make_move('b8', 'e8'))
    print("24:", game.make_move('f3', 'f1'))
    print("25:", game.make_move('i7', 'h7'))  # Blue
    print("26:", game.make_move('f1', 'c1'))
    print("27:", game.make_move('d10', 'e9'))
    print("28:", game.make_move('a4', 'b4'))
    print("29:", game.make_move('a6', 'a1'))  # Blue
    print("30:", game.make_move('c1', 'a1'))
    print("31:", game.make_move('f8', 'd10'))
    print("32:", game.make_move('d5', 'c5'))
    print("33:", game.make_move('i10', 'i6'))  # Blue
    print("34:", game.make_move('b1', 'd4'))
    print("35:", game.make_move('c7', 'c6'))
    print("36:", game.make_move('c5', 'b5'))
    print("37:", game.make_move('b10', 'd7'))  # Blue
    print("38:", game.make_move('d4', 'f7'))
    print("39:", game.make_move('g7', 'f7'))
    print("40:", game.make_move('a1', 'f1'))
    print("41:", game.make_move('g8', 'f6'))  # Blue
    print("42:", game.make_move('f1', 'f5'))
    print("43:", game.make_move('f6', 'd5'))
    print("44:", game.make_move('e3', 'e5'))
    print("45:", game.make_move('f7', 'f6'))  # Blue
    print("46:", game.make_move('f5', 'f7'))
    print("Red in check:", game.is_in_check('red'))
    print("Blue in check:", game.is_in_check('blue'))
    print("47:", game.make_move('f10', 'e10'))  # Blue
    print("Red in check:", game.is_in_check('red'))
    print("Blue in check:", game.is_in_check('blue'))
    print("48:", game.make_move('e2', 'f1'))
    print("49:", game.make_move('i6', 'i3'))  # Blue
    print("50:", game.make_move('h2', 'g2'))
    print("51:", game.make_move('i3', 'i1'))
    print("Red in check:", game.is_in_check('red'))
    print("Blue in check:", game.is_in_check('blue'))
    print("52:", game.make_move('f1', 'e2'))  # Red
    print("Red in check:", game.is_in_check('red'))
    print("Blue in check:", game.is_in_check('blue'))
    print("53:", game.make_move('f6', 'f5'))
    print("54:", game.make_move('c4', 'd4'))
    print("55:", game.make_move('f5', 'e5'))  # Blue
    print("56:", game.make_move('f7', 'd7'))
    print("57:", game.make_move('e7', 'g4'))
    print("58:", game.make_move('d4', 'd5'))
    print("59:", game.make_move('e5', 'e4'))  # Blue
    print("60:", game.make_move('d3', 'e5'))
    print("61:", game.make_move('e4', 'e3'))
    print("Red in check:", game.is_in_check('red'))
    print("Blue in check:", game.is_in_check('blue'))
    print("62:", game.make_move('e2', 'd2'))  # Red: Issue here, general not being moved
    print("63:", game.make_move('e3', 'e2'))
    print("Red in check:", game.is_in_check('red'))
    print("Blue in check:", game.is_in_check('blue'))
    print("64:", game.make_move('d2', 'd3'))
    print("65:", game.make_move('b7', 'b6'))  # Blue
    print("66:", game.make_move('f2', 'e2'))
    print("67:", game.make_move('h7', 'h6'))
    print("68:", game.make_move('b4', 'a4'))
    print("69:", game.make_move('i1', 'd1'))  # Blue
    print("70:", game.make_move('e2', 'd2'))
    print("71:", game.make_move('e8', 'e4'))
    print("72:", game.make_move('a4', 'b4'))
    print("73:", game.make_move('d1', 'f3'))  # Blue
    print(game.get_game_state())
    print("Blue wins!" if game.get_game_state() == "BLUE_WON" else "Red wins!")


def scenario_2():
    """Running this function will result in a series of inputs to the JanggiGame class that results
    in the BLUE player winning the match."""

    game = JanggiGame()
    print(game.make_move('e7', 'e6'))
    print(game.make_move('e2', 'e2'))
    print(game.make_move('e6', 'e5'))
    print(game.make_move('e2', 'e2'))
    print(game.make_move('e5', 'e4'))
    print(game.make_move('e2', 'e2'))
    print(game.make_move('e4', 'd4'))
    print(game.make_move('e2', 'e2'))
    print(game.make_move('d4', 'c4'))
    print(game.make_move('e2', 'e2'))
    print(game.make_move('a10', 'a9'))
    print(game.make_move('e2', 'e2'))
    print(game.make_move('a9', 'd9'))
    print(game.make_move('e2', 'e2'))
    print(game.make_move('d9', 'd8'))
    print(game.make_move('e2', 'e2'))
    print(game.make_move('d8', 'd7'))
    print(game.make_move('e2', 'e2'))
    print(game.make_move('d7', 'd6'))
    print(game.make_move('i1', 'i2'))
    print(game.make_move('e9', 'e9'))
    print(game.make_move('i2', 'g2'))
    print(game.make_move('e9', 'e9'))
    print(game.make_move('i4', 'h4'))
    print(game.make_move('e9', 'e9'))
    print(game.make_move('h3', 'h5'))
    print(game.make_move('i10', 'i9'))
    print(game.make_move('e2', 'e2'))
    print(game.make_move('i9', 'g9'))
    print(game.make_move('e2', 'e2'))
    print(game.make_move('g9', 'g8'))
    print(game.make_move('e2', 'e2'))
    print(game.make_move('h8', 'f8'))
    print(game.make_move('f1', 'e1'))
    print(game.make_move('g7', 'f7'))
    print(game.make_move('e2', 'e2'))
    print(game.make_move('i7', 'i6'))
    print(game.make_move('e2', 'e2'))
    print(game.make_move('g10', 'i7'))
    print(game.make_move('e2', 'e2'))
    print(game.make_move('i7', 'f5'))
    print(game.make_move('e2', 'e2'))
    print(game.make_move('f5', 'd8'))
    print(game.make_move('e2', 'e2'))
    print(game.make_move('d8', 'b5'))
    print(game.make_move('e2', 'e2'))
    print(game.make_move('c4', 'd4'))
    print(game.make_move('e2', 'e2'))
    print(game.make_move('d4', 'e4'))
    print(game.make_move('e2', 'e2'))
    # checkmate move
    print(game.make_move('e4', 'e3'))
    print(game.get_game_state())
    print("Blue wins!" if game.get_game_state() == "BLUE_WON" else "Red wins!")
