X = "X"
O = "O"
EMPTY = None

def initial_start():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    
def player(board):
    count_x = 0
    count_o = 0
    for i in board:
        for j in i:
            if j == "X":
                count_x += 1
            elif j == "O":
                count_o += 1
    
    if count_x == count_o:
        return "X"
    else:
        return "O"