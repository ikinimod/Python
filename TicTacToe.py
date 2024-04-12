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
choose_field = input("Bitte Feld eingeben: ")
choose_field = int(choose_field)
print(type(choose_field))