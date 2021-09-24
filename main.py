from termcolor import cprint
#  | | | | | |
# -------------
#  | | | | | |
# -------------
#  | | | | | |
# -------------
#  | | | | | |
# -------------
#  | | | | | |
# -------------
#  | | | | | |
# -------------
#  | | | | | |
field = [[" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " "]]

def walk_over_every_col_slant_by_left_check(board_field, start_col, stop_col, start_row, list1, list2):
    list1.clear()
    list2.clear()
    while start_col <= stop_col:
        if board_field[start_col][start_row] == " ":
            list1.clear()
            list2.clear()
        if board_field[start_col][start_row] == "X":
            list1.append("X")
            list2.clear()
            if len(list1) == 4:
                return True
        if board_field[start_col][start_row] == "O":
            list2.append("O")
            list1.clear()
            if len(list2) == 4:
                return True
        start_col += 1
        start_row += 1

def walk_over_col_slant_by_right_check(board_field, start_col, stop_col, start_row, list1, list2):
    list1.clear()
    list2.clear()
    while start_col >= stop_col: #begint op zes
        if board_field[start_col][start_row] == " ":
            list1.clear()
            list2.clear()
        if board_field[start_col][start_row] == "X":
            list1.append("X")
            list2.clear()
            if len(list1) == 4:
                return True
        if board_field[start_col][start_row] == "O":
            list2.append("O")
            list1.clear()
            if len(list2) == 4:
                return True
        start_col -= 1
        start_row += 1

def winner_slant(board_field):
    #left_check
    list_slant_x = []
    list_slant_0 = []
    for start_col in range(3, -1, -1):
        if walk_over_every_col_slant_by_left_check(board_field, start_col, 6, 0, list_slant_x,
                                                   list_slant_0):
            return True
    start_row = 0
    for stop_col in range(5, 2, -1):
        start_row += 1
        if walk_over_every_col_slant_by_left_check(board_field, 0, stop_col, start_row, list_slant_x,
                                                   list_slant_0):
            return True
    #right_check
    for start_right_col in range(3, 7):
        if walk_over_col_slant_by_right_check(board_field, start_right_col, 0, 0,
                                              list_slant_x, list_slant_0):
            return True
    start_right_row = 0
    for stop_right_col in range(1, 4):
        start_right_row += 1
        if walk_over_col_slant_by_right_check(board_field, 6, stop_right_col, start_right_row,
                                              list_slant_x, list_slant_0):
            return True

def walk_over_every_col_horizontal_check(board_field, board_row, list1, list2):
    list1.clear()
    list2.clear()
    for col in board_field:
        if col[board_row] == " ":
            list1.clear()
            list2.clear()
        if col[board_row] == "X":
            list1.append("X")
            list2.clear()
            if len(list1) == 4:
                return True
        if col[board_row] == "O":
            list2.append("O")
            list1.clear()
            if len(list2) == 4:
                return True

def winner_horizontal(board_field):
    horizontal_list_x = []
    horizontal_list_o = []
    for position in range(6, -1, -1):
        if walk_over_every_col_horizontal_check(board_field, position, horizontal_list_x, horizontal_list_o):
            return True

def winner_vertical(board_field):
    list_x = []
    list_0 = []
    for col in board_field:
        list_x.clear()
        list_0.clear()
        i = 1
        j = 1
        for row in col:
            if row == " ":
                continue
            else:
                if row == "X":
                    i += 1
                    j = 1
                    list_x.append("X")

                    if i == 5:
                        if len(list_x) == 4:
                            return True
                        else:
                            continue
                    else:
                        continue
                if row == "O":
                    j += 1
                    i = 1
                    list_0.append("O")
                    if j == 5:
                        if len(list_0) == 4:
                            return True
                        else:
                            continue
                    else:
                        continue

def return_empty_row(board_field, col):
    for row_position in range(6, -1, -1):
        if board_field[col][row_position] == " ":
            return row_position

def draw_connect_4_board(board_field):
    for row in range(13):
        if row % 2 == 0:
            practical_row = int(row / 2)
            for column in range(13):
                    if column % 2 == 0:
                        practical_column = int(column / 2)
                        if column != 12:
                            cprint(board_field[practical_column][practical_row], 'red', end='') #grey, red, green, yellow, blue, magenta,cyan, white
                        else:
                            cprint(board_field[practical_column][practical_row], 'red')
                    else:
                        print("|", end="")
        else:
            print("-------------")

def check_col(col):
    return 0 <= col <= 6

draw_connect_4_board(field)
player = 1

while True:
    if player == 1:
        column_player = int(input("Player 1 - Column: "))
        column_player -= 1
        if check_col(column_player):
            row = return_empty_row(field, column_player)
            if row is not None:
                field[column_player][row] = "X"
                if winner_vertical(field):
                    draw_connect_4_board(field)
                    print(f"Player {player}, you win the game with a vertical 4 in a row")
                    break
                if winner_horizontal(field):
                    draw_connect_4_board(field)
                    print(f"Player {player}, you win the game with a horizontal 4 in a row")
                    break
                if winner_slant(field):
                    draw_connect_4_board(field)
                    print(f"Player {player}, you win the game with a slanted four in a row")
                    break
                player = 2
            else:
                print("You can't put more in here")
    else:
        column_player = int(input("Player 2 - Column: "))
        column_player -= 1
        if check_col(column_player):
            row1 = return_empty_row(field, column_player)
            if row1 is not None:
                field[column_player][row1] = "O"
                if winner_vertical(field):
                    draw_connect_4_board(field)
                    print(f"Player {player}, you win the game with a vertical 4 in a row")
                    break
                if winner_horizontal(field):
                    draw_connect_4_board(field)
                    print(f"Player {player}, you win the game with a horizontal 4 in a row")
                    break
                if winner_slant(field):
                    draw_connect_4_board(field)
                    print(f"Player {player}, you win the game with a slanted four in a row")
                    break
                player = 1
            else:
                print("You can't put more in here")
    draw_connect_4_board(field)
