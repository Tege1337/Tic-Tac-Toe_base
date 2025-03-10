def get_menu_option():
  '''
  Should print a menu with the following options:
  1. Human vs Human
  2. Random AI vs Random AI
  3. Human vs Random AI
  4. Human vs Unbeatable AI

  The function should return a number between 1-4.
  If the user will enter invalid data (for example 5), than a message will appear
  asking to input a new value.
  '''

  while valaszt:
    option = input( "1. Human vs Human\n"
                      "2. Random AI vs Random AI\n"
                      "3. Human vs Random AI\n"
                      "4. Human vs Unbeatable AI\n"
                      "Type 1, 2, 3 or 4. ")
      
    if option is None or option == " ":
      valaszt = True
    elif option == "1" or option == "2" or option == "3" or option == "4":
      valaszt = False
      
      
      
      return option



if __name__ == "__main__":
    option = get_menu_option()
    print(option) 