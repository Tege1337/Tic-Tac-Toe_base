import random

# TIKTOKTOE.py
# pálya generálás
mezo = []
sor = []
for i in range(3):
    for j in range(3):
        sor.append(" ")
    mezo.append(sor)
    sor = []

# mező kiírása
def print_mezo():
    for i in range(3):
        print(" " + " | ".join(mezo[i]) + " ")
        if i < 2:
            print("---+---+---")

# játékos választás
def player_turn(turn_player1, ai_mode):
    if turn_player1:
        turn_player1 = False
        if ai_mode:
            print(f"A gép van soron!")
        else:
            print(f"{player2} van soron!")
    else:
        turn_player1 = True
        print(f"{player1} van soron!")
    return turn_player1

# mező választása
def write_cell(cell):
    cell -= 1
    i = cell // 3
    j = cell % 3
    if turn_player1:
        mezo[i][j] = player1_symbol
    else:
        mezo[i][j] = player2_symbol
    return mezo

# mező szabad-e?
def free_cell(cell):
    cell -= 1
    i = cell // 3
    j = cell % 3
    if mezo[i][j] in [player1_symbol, player2_symbol]:
        print("HÉ! Ez egy foglalt cella...")
        return False
    return True

# AI lépés
def ai_move():
    for cell in range(1, 10):
        cell -= 1
        i, j = cell // 3, cell % 3
        if mezo[i][j] == " ":
            mezo[i][j] = player2_symbol
            game_check, _ = win_check(mezo, player1_symbol, player2_symbol)
            mezo[i][j] = " "
            if not game_check:  # Ha AI nyerhet, lépjen ide
                return cell + 1
    # Nincs nyerő lépés, válassz véletlenszerűen
    empty_cells = [idx + 1 for idx in range(9) if mezo[idx // 3][idx % 3] == " "]
    return random.choice(empty_cells)

# játék eleje
print("\n\n🦠 KUTYÁK - TIKTOKTOE!\n\n")

def get_symbol(player):
    while True:
        symbol = input(f"Értem {player}, milyen szimbólummal játszol? (Csak 1 karakter!) : ")
        if len(symbol) == 1:
            return symbol
        else:
            print("Hibás bemenet! Csak 1 karaktert választhatsz.")

player1 = input("Első játékos, mi a neved? : ")
player1_symbol = get_symbol(player1)

# Játékmód választása
mode = input("Szeretnél AI ellen játszani? (igen/nem) : ").strip().lower()
ai_mode = mode == 'igen'

if ai_mode:
    player2 = "Gép"
    player2_symbol = get_symbol(player2)
else:
    player2 = input("Második játékos, hogyan szólíthatlak? : ")
    player2_symbol = get_symbol(player2)

print(f"*------------------*\nJáték információk:\n\nElső játékos:\n{player1} - {player1_symbol}\n\nMásodik játékos:\n{player2} - {player2_symbol}\n\n*------------------*")

game = True
turn_player1 = False
winner = ""

# nyerés ellenőrzése
def win_check(mezo, player1_symbol, player2_symbol):
    full_mezo = True
    lines = [  # Sorok, oszlopok, átlók
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]

    for line in lines:
        symbols = [mezo[i][j] for i, j in line]
        if symbols == [player1_symbol]*3:
            return False, player1
        if symbols == [player2_symbol]*3:
            return False, player2

    for row in mezo:
        if " " in row:
            full_mezo = False

    if full_mezo:
        return False, ""  # Döntetlen

    return True, ""

# játék fő ciklusa
while game:
    turn_player1 = player_turn(turn_player1, ai_mode)

    valid_move = False
    while not valid_move:
        if turn_player1 or not ai_mode:
            try:
                cell = int(input("Válassz cellát (1-9): "))
                if 1 <= cell <= 9 and free_cell(cell):
                    valid_move = True
            except ValueError:
                print("Kérlek, adj meg egy számot 1 és 9 között.")
        else:
            cell = ai_move()
            print(f"A gép a(z) {cell} cellát választja.")
            valid_move = True

    mezo = write_cell(cell)
    print_mezo()
    game, winner = win_check(mezo, player1_symbol, player2_symbol)

# játék vége
if winner == player1:
    print(f"🎉 {player1}, gratulálok, nyertél!")
elif winner == player2:
    print(f"🎉 {player2}, gratulálok, nyertél!")
else:
    print("🪦 DÖNTETLEN!")
