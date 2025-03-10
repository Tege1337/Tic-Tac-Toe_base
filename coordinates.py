def get_human_coordinates(board, current_player):
    """
    Reads valid coordinates from the user for a tic-tac-toe game.
    """
    valid_letters = {'A': 0, 'B': 1, 'C': 2}
    valid_numbers = {'1': 0, '2': 1, '3': 2}
    
    while True:
        user_input = input(f"Player {current_player}, enter your move (e.g., A1, B2) or 'quit' to exit: ").strip().upper()
        
        if user_input == "QUIT":
            print("Game exited.")
            exit()
        
        if len(user_input) == 2 and user_input[0] in valid_letters and user_input[1] in valid_numbers:
            row, col = valid_letters[user_input[0]], valid_numbers[user_input[1]]
            
            if board[row][col] == ' ':  # Assuming empty spaces are represented as ' '
                return row, col
            else:
                print("That spot is already taken. Please try again.")
        else:
            print("Invalid input. Please enter a valid coordinate (e.g., A1, B2). Try again.")






def get_random_ai_coordinates(board, current_player):
  """
  Should return a tuple of 2 numbers. 
  Each number should be between 0-2.
  The chosen number should be only a free coordinate from the board.
  If the board is full (all spots taken by either X or O) than "None"
  should be returned.
  """
  # ez nem kell
  pass


def get_unbeatable_ai_coordinates(board, current_player):
  """
  Should return a tuple of 2 numbers. 
  Each number should be between 0-2.
  The chosen number should be only a free coordinate from the board.
  The chosen coordinate should always stop the other player from winning or
  maximize the current player's chances to win.
  If the board is full (all spots taken by either X or O) than "None"
  should be returned.
  """
  # ez se
  pass


# run this file to test whether you have correctly implemented the functions
if __name__ == "__main__":
  board_1 = [
    ["X", "X", "."],
    ["X", ".", "."],
    ["X", "X", "."],
  ]
  print("It should print the coordinates selected by the human player")
  coordinates = get_human_coordinates(board_1, "X")
  print(coordinates)

  board_2 = [
    ["O", "O", "."],
    ["X", "O", "."],
    ["X", "X", "O"],
  ]
  print("The printed coordinate should be only (0,2) or (1,2)")
  print(get_random_ai_coordinates(board_2))
  print("The printed coordinate should be only (0,2) or (1,2)")
  print(get_random_ai_coordinates(board_2))
  print("The printed coordinate should be only (0,2) or (1,2)")
  print(get_random_ai_coordinates(board_2))

  board_3 = [
    ["O", "X", "X"],
    ["X", "O", "X"],
    ["X", "O", "X"],
  ]
  print("The printed coordinate should be None")
  print(get_random_ai_coordinates(board_3))

  board_4 = [
    [".", "O", "."],
    ["X", "O", "."],
    ["X", "X", "O"],
  ]
  print("The printed coordinate should always be (0, 0)")
  print(get_unbeatable_ai_coordinates(board_4, "X")) 

  board_5 = [
    ["X", "O", "."],
    ["X", ".", "."],
    ["O", "O", "X"],
  ]
  print("The printed coordinate should always be (1, 1)")
  print(get_unbeatable_ai_coordinates(board_5, "O")) 

  board_6 = [
    ["O", "O", "."],
    ["O", "X", "."],
    [".", "X", "."],
  ]
  print("The printed coordinate should either (0, 2) or (2, 0)")
  print(get_unbeatable_ai_coordinates(board_6)) 