# This is a portfolio project. I will try to make a tictactoe game with python respectively obcejt orientated programming.

running = True
active_player = "X"

field = [" ",
             "1","2","3",
             "4","5","6",
             "7","8","9"]

# field printing
# print (field[1] + "|" + field[2] + "|" + field[3] )
# print (field[4] + "|" + field[5] + "|" + field[6] )
# print (field[7] + "|" + field[8] + "|" + field[9] )

# Printing field function
def print_field():
    print (field[1] + "|" + field[2] + "|" + field[3] )
    print (field[4] + "|" + field[5] + "|" + field[6] )
    print (field[7] + "|" + field[8] + "|" + field[9] )
print_field()

#User Input
def user_input():
    global running
    while True:
        choose_field = input("Choose your field: ")
        if choose_field == q:
             running = False
             return
        try:
            choose_field = int(choose_field)
        except ValueError:
            print("Please put a number between 1 to 9")
        else:
            if choose_field >= 1 and choose_field <= 9:
                  return choose_field
            else:
                  print("Number is not between 1 to 9")

def switch_player():
     global active_player
     if active_player == "X":
          active_player = "O"
     else:
          active_player = "X"

print_field()
while running:
     print("Player" + active_player + "move")
     choose_field = user_input()
     if choose_field:
          field[choose_field] = active_player
          print_field()
          switch_player()

# choose_field = user_input()
# print("Field: " + str(choose_field))