def get_empty_board():
    """Visszaad egy üres 3x3-as táblát."""
    return [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def display_board(board):
    """Megjeleníti a táblát olvasható formában."""
    print("    1   2   3")
    for i, sor in enumerate(board):
        sorszam = chr(ord('A') + i)  # A, B, C sorok
        print(f"  {sorszam}  {sor[0]} | {sor[1]} | {sor[2]}")
        if i < 2:
            print("    ---+---+---")  # Elválasztó vonal

def is_board_full(board):
    """Visszaadja, hogy a tábla tele van-e (nincs üres hely)."""
    for row in board:
        if ' ' in row:  # Ha van üres mező
            return False
    return True  # Ha nincs üres mező, a tábla tele van

def get_winning_player(board):
    """
    Visszaadja a nyertes játékost ('X' vagy 'O'), vagy None-t, ha nincs nyertes.
    """

    # Ellenőrizzük a sorokat
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '.':
            return row[0]

    # Ellenőrizzük az oszlopokat
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '.':
            return board[0][col]

    # Ellenőrizzük az 
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '.':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '.':
        return board[0][2]

    return None  # Ha nincs 

# Teszt kód
if __name__ == "__main__":
    empty_board = get_empty_board()
    print(empty_board)

    board = [
      ['X', 'O', '.'],
      ['X', 'O', '.'],
      ['0', 'X', '.'],
    ]
    print("Should print the board:")
    display_board(board)

    # Tesztelés
    board_1 = [
      ['X', 'O', '.'],
      ['X', 'O', '.'],
      ['X', 'X', 'O'],
    ]
    print("Should return False (tábla nincs tele):", is_board_full(board_1)) 

    board_2 = [
      ['.', 'O', 'O'],
      ['.', 'O', 'X'],
      ['.', 'X', 'X'],
    ]
    print("Should return False (tábla nincs tele):", is_board_full(board_2))

    board_3 = [
      ['O', 'O', 'X'],
      ['O', 'X', 'O'],
      ['O', 'X', 'X'],
    ]
    print("Should return True (tábla tele van):", is_board_full(board_3))

    board_4 = [
      ['X', 'O', '.'],
      ['X', 'O', '.'],
      ['X', 'X', 'O'],
    ]
    print("Should return X (X nyert):", get_winning_player(board_4))

    board_5 = [
      ['X', 'O', 'O'],
      ['X', 'O', '.'],
      ['O', 'X', 'X'],
    ]
    print("Should return O (O nyert):", get_winning_player(board_5))

    board_6 = [
      ['O', 'O', '.'],
      ['O', 'X', '.'],
      ['.', 'X', '.'],
    ]
    print("Should return None (nincs nyertes):", get_winning_player(board_6))

