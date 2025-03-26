# TIKTOKTOE.py × KUTYÁK
import random
import time

# kordik 
cell_mapping = {
    "A1": (0, 0), "A2": (0, 1), "A3": (0, 2),
    "B1": (1, 0), "B2": (1, 1), "B3": (1, 2),
    "C1": (2, 0), "C2": (2, 1), "C3": (2, 2)
}

# pálya generálás
mezo = []
sor = []
for i in range(3):
    for j in range(3):
        sor.append(" ")
    mezo.append(sor)
    sor = []

# mezo kiirasa
def print_mezo():
    print("\n    1   2   3")
    print("  ┌───┬───┬───┐")
    for i, row in enumerate(mezo):
        row_label = chr(65 + i)  # 0 1 2 - A B C 
        print(f"{row_label} │ " + " │ ".join(row) + " │")
        if i < 2:
            print("  ├───┼───┼───┤")
    print("  └───┴───┴───┘\n")

# játékos választás
def player_turn(turn_player1, ai_mode):
    if turn_player1:
        turn_player1 = False
        if ai_mode:
            print("\n🔹 A gép gondolkodik...")
        else:
            print(f"\n🔸 {player2} van soron!")
    else:
        turn_player1 = True
        print(f"\n🔸 {player1} van soron!")
    return turn_player1

# cellaba iras
def write_cell(cell):
    i, j = cell_mapping[cell]
    symbol = player1_symbol if turn_player1 else player2_symbol
    mezo[i][j] = symbol
    return mezo

# cella-szabad-e
def free_cell(cell):
    if cell not in cell_mapping:
        print("⚠️  Érvénytelen cella! Próbáld újra.")
        return False
    i, j = cell_mapping[cell]
    if mezo[i][j] in [player1_symbol, player2_symbol]:
        print("⚠️  Ez a cella már foglalt! Próbáld újra.")
        return False
    return True

# ai mode
def ai_move():
    for cell, (i, j) in cell_mapping.items():
        if mezo[i][j] == " ":
            mezo[i][j] = player2_symbol
            game_check, _ = win_check(mezo, player1_symbol, player2_symbol)
            mezo[i][j] = " "
            if not game_check:  # Ha az AI nyerhet
                return cell
    empty_cells = [cell for cell, (i, j) in cell_mapping.items() if mezo[i][j] == " "]
    return random.choice(empty_cells)

# játék eleje
print("\n🦠 KUTYÁK - TIKTOKTOE! 🦠\n")

def get_symbol(player):
    while True:
        symbol = input(f"🎮 {player}, válassz szimbólumot (1 karakter!): ").strip()
        if len(symbol) == 1:
            return symbol
        print("⚠️  Hibás bemenet! Csak 1 karaktert választhatsz.")

player1 = input("👤 Első játékos, mi a neved? ").strip()
player1_symbol = get_symbol(player1)

mode = input("🕹 AI ellen játszol? (igen/nem) ").strip().lower()
ai_mode = mode == 'igen'

if ai_mode:
    player2 = "Gép"
    while True:
        player2_symbol = get_symbol(player2)
        if player2_symbol != player1_symbol:
            break
        print("⚠️  Ez a szimbólum már foglalt az első játékos által! Válassz másikat.")
else:
    player2 = input("👤 Második játékos, hogy hívhatlak? ").strip()
    while True:
        player2_symbol = get_symbol(player2)
        if player2_symbol != player1_symbol:
            break
        print("⚠️  Ez a szimbólum már foglalt az első játékos által! Válassz másikat.")

print(f"\n*--------------------*\n  Játék információk:\n\n  1. {player1}: {player1_symbol}\n  2. {player2}: {player2_symbol}\n*--------------------*\n")
time.sleep(2)

game = True
turn_player1 = False
winner = ""

def win_check(mezo, p1_sym, p2_sym):
    lines = [
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
        if symbols == [p1_sym]*3:
            return False, player1
        if symbols == [p2_sym]*3:
            return False, player2

    if all(cell != " " for row in mezo for cell in row):
        return False, ""  # Döntetlen

    return True, ""

# jatek ciklus
while game:
    print_mezo()
    turn_player1 = player_turn(turn_player1, ai_mode)
    
    valid_move = False
    while not valid_move:
        if turn_player1 or not ai_mode:
            try:
                cell = input("🔢 Válassz cellát (pl. A1, B2): ").strip().upper()
                if free_cell(cell):
                    valid_move = True
            except ValueError:
                print("⚠️  Érvénytelen bemenet!")
        else:
            time.sleep(1.5)
            cell = ai_move()
            print(f"🤖 A gép a(z) {cell} cellát választotta.")
            valid_move = True

    mezo = write_cell(cell)
    game, winner = win_check(mezo, player1_symbol, player2_symbol)

# A játék vége
print_mezo()
if winner == player1:
    print(f"🎉 {player1}, nyertél! Gratulálok!")
elif winner == player2:
    print(f"🎉 {player2}, a gép nyert! Próbáld újra!")
else:
    print("⚖️ Döntetlen! Próbáljátok meg újra!")
