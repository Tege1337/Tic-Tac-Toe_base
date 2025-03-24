#Pálya létrehozása
oszlop = []
sor = []

for i in range(3):
    for j in range(3):
        sor.append(" ")
    oszlop.append(sor)
    sor = []
         

#Pálya kiírása
def print_grid():
    for x in range(3):
        print('|', end="")
        for y in range(3):
            print(grid[x][y], "|", end="")
            print()
            

#Játékos
def player_turn(turn_player1):
    if turn_player1 == True:
        turn_player1 = False


def write_cell(cell)