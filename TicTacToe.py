# This is a portfolio project. I will try to make a tictactoe game with python respectively obcejt orientated programming.
print("Tic-Tac-Toe Python")

running = True
active_player = "X"

# Creating field as list
field = [" ",
             "1","2","3",
             "4","5","6",
             "7","8","9"]


# Field function
def print_field():
    print (field[1] + "|" + field[2] + "|" + field[3] )
    print (field[4] + "|" + field[5] + "|" + field[6] )
    print (field[7] + "|" + field[8] + "|" + field[9] )

#User input + control
def user_input():
    global running
    while True:
        choose_field = input("Choose your field: ")
        if choose_field == "q":
             running = False
             return
        try:
            choose_field = int(choose_field)
        except ValueError:
            print("Please put a number between 1 to 9")
        else:
            if choose_field >= 1 and choose_field <= 9:
                  if field[choose_field] == "X" or field[choose_field] == "O":
                       print(" Field has already been used - choose another one!")
                  else:
                      return choose_field
            else:
                  print("Number is not between 1 to 9")

def switch_player():
     global active_player
     if active_player == "X":
          active_player = "O"
     else:
          active_player = "X"

# Function that controls win status
def check_win():
     # Check rows
     if field[1] == field[2] == field[3]:
          return field[1]
     if field[4] == field[5] == field[6]:
          return[4]
     if field[7] == field[8] == field[9]:
          return[7]
     # Check columns
     if field[1] == field[4] == field[7]:
          return field[1]
     if field[2] == field[5] == field[8]:
          return[2]
     if field[3] == field[6] == field[9]:
          return[3]
     # Check diagonal
     if field[1] == field[5] == field[9]:
          return[5]
     if field[7] == field[5] == field[3]:
          return[5]

# Function that check if it is a draw
def check_draw():
     if (field[1] == "X" or field[1] == "O") \
     and (field[2] == "X" or field[2] == "O") \
     and (field[3] == "X" or field[3] == "O") \
     and (field[4] == "X" or field[4] == "O") \
     and (field[5] == "X" or field[5] == "O") \
     and (field[6] == "X" or field[6] == "O") \
     and (field[7] == "X" or field[7] == "O") \
     and (field[8] == "X" or field[8] == "O") \
     and (field[9] == "X" or field[9] == "O"):
          return("Draw!")

# Output active field
print_field()
while running:
     print()
     print("Player " + active_player + " move")
     choose_field = user_input()
     if choose_field:
          field[choose_field] = active_player
          # Current field
          print_field()
          # Check, if win
          winner = check_win()
          if winner:
               print("Player " + winner + " has won!")
               running = False
               break
          # Check, if draw
          draw = check_draw()
          if draw:
               print("This game is a draw!")
               running = False
           # Switch player    
          switch_player()
print()          

