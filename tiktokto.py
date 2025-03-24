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
    for i in range(3):
        print('|', end="")
        for j in range(3):
            print(oszlop[i][j], "|", end="")
            print()
            

#Játékos
def player_turn(turn_player1):
    if turn_player1 == True:
        turn_player1 = False
        print(f"{player2} a soros")
    else:
        turn_player1 = True
        print(f"{player1} a soros")
    return turn_player1


#hely kiválasztása
def write_cell(cell):
    cell -= 1
    i = int(cell / 3)
    j =  cell % 3   
    if turn_player1 == True:
        oszlop[i][j] = player1_symbol
    else:
        oszlop[i][j] = player2_symbol
    return oszlop


#megnézi hoogy szabad e a hely
def free_cell(cell):
    cell -= 1
    i = int(cell / 3)
    j =  cell % 3
    if oszlop[i][j] == player1_symbol or groslopid[i][j] == player2_symbol:
        print("This cell is not free")
        return False
    return True


print("TIC-TAC-TOE")
player1 = input("Kérlek add meg az első játékos nevét! ")
player1_symbol = input("Kérlek add meg az első játékos szimbólumát! ")
player2 = input("Kérlek add meg a második játékos nevét! ")
player2_symbol = input("Kérlek add meg a második játékos szimbólumát! ")

game = True
full_grid = False
turn_player1 = False
winner = ""


while game == True:
    turn_player1 = player_turn(turn_player1)
    free_box = False
    while free_box == False:
        cell = int(inu