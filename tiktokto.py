#palya generalas
mezo = []
sor = []
for i in range (3):
    for j in range (3):
        sor.append(" ")
    mezo.append(sor)
    sor = []
 
#mezo kiirás
def print_mezo():
    for i in range(3):
        # Sorok kiírása
        print(" " + " | ".join(mezo[i]) + " ")
        if i < 2:
            print("---+---+---")  # A sorok között elválasztó

#jatekos kivalasztas
def player_turn(turn_player1):
    if turn_player1 == True:
        turn_player1 = False
        print(f"{player2} van soron! ")
    else:
        turn_player1 = True
        print(f"{player1} van soron! ")        
    return turn_player1
 
#mezo kivalasztasa
def write_cell(cell):
    cell -= 1
    i = int(cell / 3)
    j =  cell % 3   
    if turn_player1 == True:
        mezo[i][j] = player1_symbol
    else:
        mezo[i][j] = player2_symbol
    return mezo
 
#szabad e a mezo
def free_cell(cell):
    cell -= 1
    i = int(cell / 3)
    j =  cell % 3
    if mezo[i][j] == player1_symbol or mezo[i][j] == player2_symbol:
        print("HÉ! Ez egy foglalt cella...")
        return False
    return True
 
#játék eleje
print("🦠 KUTYÁK - TIKTOKTOE!")
print("")
print_mezo()
print("")
player1 = input("Első játékos, most hozzád szólok, mi a neved? : ")
player1_symbol = input(f"Értem {player1} és mégis milyen szimbólummal fogsz játszani? : ")
player2 = input("Na és most te jössz második játékos! Hogyan szólíthatlak?: ")
player2_symbol = input(f"Ahha, tehát {player2}, szia! És te melyik szimbólumot választottad? : ")
print(f"*------------------*\nJáték információk:\n\nElső játékos:\n{player1} - {player1_symbol}\n\nMásodik játékos:\n{player2} - {player2_symbol}\n\n*------------------*")
game = True
full_mezo = False
turn_player1 = False
winner = ""
 
#nyeres
def win_check(mezo, player1_symbol, player2_symbol):
    full_mezo = True
    player1_symbol_count = 0
    player2_symbol_count = 0
    #sor
    for i in range(3):
        for j in range(3):
            if mezo[i][j] == player1_symbol:
                player1_symbol_count += 1
                player2_symbol_count = 0
                if player1_symbol_count == 3:
                    game = False
                    winner = player1
                    return game, winner
            if mezo[i][j] == player2_symbol:
                player2_symbol_count += 1
                player1_symbol_count = 0
                if player2_symbol_count == 3:
                    game = False
                    winner = player2
                    return game, winner
            if mezo[i][j] == " ":
                full_mezo = False
                 
        player1_symbol_count = 0
        player2_symbol_count = 0
    #oszlop
    player1_symbol_count = 0
    player2_symbol_count = 0    
    for i in range (3):
        for j in range (3):
            for k in range (3):
                if i + k <= 2:
                    if mezo[i + k][j] == player1_symbol:
                        player1_symbol_count += 1
                        player2_symbol_count = 0
                        if player1_symbol_count == 3:
                            game = False
                            winner = player1
                            return game, winner
                    if mezo[i + k][j] == player2_symbol:
                        player2_symbol_count += 1
                        player1_symbol_count = 0
                        if player2_symbol_count == 3:
                            game = False
                            winner = player2
                            return game, winner
            if mezo[i][j] == " ":
                full_mezo = False
 
            player1_symbol_count = 0
            player2_symbol_count = 0
    #átlós
    player1_symbol_count = 0
    player2_symbol_count = 0    
    for i in range (3):
        for j in range (3):
            for k in range (3):
                if j + k <= 2 and i + k <= 2:
                    if mezo[i + k][j + k] == player1_symbol:
                        player1_symbol_count += 1
                        player2_symbol_count = 0
                        if player1_symbol_count == 3:
                            game = False
                            winner = player1
                            return game, winner
                    if mezo[i + k][j + k] == player2_symbol:
                        player2_symbol_count += 1
                        player1_symbol_count = 0
                        if player2_symbol_count == 3:
                            game = False
                            winner = player2
                            return game, winner
            if mezo[i][j] == " ":
                full_mezo = False
             
            player1_symbol_count = 0
            player2_symbol_count = 0
             
    player1_symbol_count = 0
    player2_symbol_count = 0    
    for i in range (3):
        for j in range (3):
            for k in range (3):
                if j - k >= 0 and i + k <= 2:
                    if mezo[i + k][j - k] == player1_symbol:
                        player1_symbol_count += 1
                        player2_symbol_count = 0
                        if player1_symbol_count == 3:
                            game = False
                            winner = player1
                            return game, winner
                    if mezo[i + k][j - k] == player2_symbol:
                        player2_symbol_count += 1
                        player1_symbol_count = 0
                        if player2_symbol_count == 3:
                            game = False
                            winner = player2
                            return game, winner
            if mezo[i][j] == " ":
                full_mezo = False
         
            player1_symbol_count = 0
            player2_symbol_count = 0              
         
    #tele van a palya
    if full_mezo == True:
        game = False
        winner = ""
        return game, winner
    else:
        game = True
        winner = ""
        return game, winner
 
#gém
while game == True:
    turn_player1 = player_turn(turn_player1)
    free_box = False
    while free_box == False:
        cell = int(input("\nKérlek add meg a választott cellát (1-9) : "))
        free_box = free_cell(cell)
    mezo = write_cell(cell)
    print_mezo()
    game, winner = win_check(mezo, player1_symbol, player2_symbol)
     
#játék vége
if winner == player1:
    print(f"\n🎉 {player1}, gratuálok, nyertél!")
elif winner == player2:
    print(f"\n🎉 {player2}, gratuálok, nyertél!")
else:
    print(f"\n🪦 DÖNTETLEN")
