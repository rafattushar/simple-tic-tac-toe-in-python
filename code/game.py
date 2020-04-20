import itertools

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]



def win(current_game):
    def sameValueCheck(lst):
        if len(set(lst)) <= 1 and lst[0] != 0:
            return True
        else:
            return False
    
    # Dialonal 
    valueL = []
    ind = list(range(len(current_game)))
    for col, row in enumerate(ind):
        valueL.append(current_game[row][col])
    if sameValueCheck(valueL):
        print(valueL)
        print(f"Player {valueL[0]} has won diagonally (\\)")
        return True
        
    valueR = []
    row = list(reversed(range(len(game))))
    for col in ind:
        valueR.append(game[col][row[col]])
    if sameValueCheck(valueR):
        print(valueR)
        print(f"Player {valueR[0]} has won diagonally (/)")
        return True
    
    # Horizontal
    for row in current_game:
        if sameValueCheck(row):
            print(row)
            print(f"Player {row[0]} has won Horizontally (--)")
            return True
            
    # Vertical
    for col in range(len(game[0])):
        value = []
        for row in current_game:
            value.append(row[col])
            
        if sameValueCheck(value):
            print(value)
            print(f"Player {value[0]} has won vertically (|)")
            return True

def game_board(game_map, player = 1, row = 0, col = 0, just_display = False):
    try:
        if game_map[row][col] != 0 and just_display == False:
            print("The place is already occupied. Choose another")
            return game_map, False, False
        if just_display == False and game_map[row][col] == 0:
            game_map[row][col] = player
        print("   0  1  2")
        isFull = True
        for count, row in enumerate(game_map):
            for col in row:
                if col == 0:
                    isFull = False
                    break
            print(count, row)
        if isFull:
            print("No remaining place. Exiting...")
            return game_map, True, True
        return game_map, True, False
    except IndexError as e:
        print("Your input is greater than 2 -", e)
        return game_map, False, False
    except Exception as e:
        print("Something went wrong!!!", e)
        return game_map, False, False

play = True
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    
    playerCategory = itertools.cycle([1, 2])
    gameWon = False
    game_board(game, just_display = True)
    isFull = False
    while (not gameWon) and (not isFull):
        selectedPlayer = next(playerCategory)
        successInput = False
        while not successInput:
            print(f"Selected Player is: {selectedPlayer}")
            rowChoice = int(input("Enter the row number: "))
            colChoice = int(input("Enter the col number: "))
            game , successInput, isFull = game_board(game, selectedPlayer, rowChoice, colChoice, False)
        ret = win(game)
        if ret:
            break
    play = int(input("Do you want play again? "))
        
    
#game_board(game_map = game, row = 2, just_display = False)
