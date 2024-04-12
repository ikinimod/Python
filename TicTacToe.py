# This is a portfolio project. I will try to make a tictactoe game with python respectively obcejt orientated programming.

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
choose_field = input("Choose your field: ")
choose_field = int(choose_field)
print(type(choose_field))

def user_input():
    while True:
        choose_field = input("Choose your field: ")
        try:
            choose_field = int(choose_field)
        except ValueError:
            print("Please put a number between 1 to 9")
        else:
            if choose_field >= 1 and choose_field <= 9:
                  return choose_field
            else:
                  print("Number is not between 1 to 9")

choose_field = user_input()
print("Field: " + str(choose_field))