#mini project
game_board = [[" ", " ", " "], 
              [" ", " ", " "], 
              [" ", " ", " "]]

def display_board(game_board): 
    """To display the Tic Tac Toe board (GUI)."""
    print("*************")
    for i in range(len(game_board)):
        print("*", end = "")
        for j in range(len(game_board[i])):
            print(f" {game_board[i][j]} ", end = "")
            if j < len(game_board[i])-1:
                print("|", end ="")
        print("*")
        print("*---|---|---*")
    print("*************")


def player_input(player): 
    """To get the position from the player."""
    pl = {1: "X",2 : "O"}
    print("Player ", pl[player], "'s turn...", sep="")
    x = int(input("Enter row: "))
    y = int(input("Enter column: "))
    while game_board[x-1][y-1] != " ":
        x = int(input("Enter row: "))
        y = int(input("Enter column: "))
    
    if player == 1:
        game_board[x-1][y-1] = "X"
    else:
        game_board[x-1][y-1] = "O"
    return x,y

def check_win(game_board, player):
    """To check whether there is a winner or not."""
    win = False
    pl = {1: "X",2 : "O"}
    # check horisontal on line
    for i in range(len(game_board)):
  #      print(game_board[i].count(pl[player]))
        if game_board[i].count(pl[player]) == 3:
            win = True

    # check vertical on line
    for j in range(len(game_board[0])):
        s = []
        for i in range(len(game_board)):
            s.append(game_board[i][j])
 #           print (s)
            if s.count(pl[player]) == 3:
                win = True
    # check diagonal on line
    s = []
    for i in range(len(game_board[0])):
        s.append(game_board[i][i])
        if s.count(pl[player]) == 3:
            win = True

    # check diagonal on line
    s = []
    for i in range(len(game_board[0])):
        s.append(game_board[i][2-i])
        if s.count(pl[player]) == 3:
            win = True
    return win

def play():
    """The main function, which calls all the functions created above."""

    flag = False
    pl = {1: "X",2 : "O"}
    display_board(game_board)
    current_player = 1
    
    while not flag:
        player_input(current_player)
        flag = check_win(game_board, current_player)
        display_board(game_board)
        if flag:
            print("Winner is ", pl[current_player])

        # check all square are full
        if sum([num.count("X") for num in [num for num in game_board]]) + sum([num.count("O") for num in [num for num in game_board]]) == 9:
            print("Game over: Tie")
            flag = True
        
        # changing turn in the game
        if current_player == 1:
            current_player = 2
        else:
            current_player = 1
        

play()