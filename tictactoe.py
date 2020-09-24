# write your code here
symbols = [" " for symbol in range(9)]
field = [[symbols[6], symbols[3], symbols[0]], [symbols[7], symbols[4], symbols[1]],
         [symbols[8], symbols[5], symbols[2]]]


def display_field():
    print("---------")
    print("|", field[0][2], field[1][2], field[2][2], "|")
    print("|", field[0][1], field[1][1], field[2][1], "|")
    print("|", field[0][0], field[1][0], field[2][0], "|")
    print("---------")


def symbol_counter(symbol_to_find):
    counter = 0
    for column in field:
        for symbol in column:
            if symbol == symbol_to_find:
                counter += 1
    return counter


def win(symbol):
    return (field[0][2] == symbol and field[1][2] == symbol and field[2][2] == symbol) or \
           (field[0][1] == symbol and field[1][1] == symbol and field[2][1] == symbol) or \
           (field[0][0] == symbol and field[1][0] == symbol and field[2][0] == symbol) or \
           (field[0][2] == symbol and field[0][1] == symbol and field[0][0] == symbol) or \
           (field[1][2] == symbol and field[1][1] == symbol and field[1][0] == symbol) or \
           (field[2][2] == symbol and field[2][1] == symbol and field[2][0] == symbol) or \
           (field[0][2] == symbol and field[1][1] == symbol and field[2][0] == symbol) or \
           (field[0][0] == symbol and field[1][1] == symbol and field[2][2] == symbol)


def not_finished():
    empty = symbol_counter(" ")
    return not win("X") and not win("O") and empty > 0


def draw():
    return not win("X") and not win("O") and not not_finished()


def impossible():
    count = abs(symbol_counter("X") - symbol_counter("O"))
    return (win("X") and win("O")) or count > 1


def result_check():
    if impossible():
        print("Impossible")
    elif not_finished():
        print("Game not finished")
    elif draw():
        print("Draw")
    elif win("X"):
        print("X wins")
    elif win("O"):
        print("O wins")


def move(o_move):
    numbers = "1234567890"
    while True:
        coordinates = input("Enter the coordinates: > ")
        coordinates = coordinates.split(" ")

        x = coordinates[0]
        y = coordinates[1]

        if not numbers.__contains__(x) or not numbers.__contains__(y):
            print("You should enter numbers!")
            continue

        x = int(x)
        y = int(y)

        if x < 1 or x > 3 or y < 1 or y > 3:
            print("Coordinates should be from 1 to 3!")
            continue

        x -= 1
        y -= 1

        if field[x][y] == "X" or field[x][y] == "O":
            print("This cell is occupied! Choose another one!")
            continue

        if o_move:
            field[x][y] = "O"
        else:
            field[x][y] = "X"

        return


def game():
    turn = True
    while True:

        if win("X"):
            print("X wins")
            break
        elif win("O"):
            print("O wins")
            break
        elif draw():
            print("Draw")
            break
        else:
            turn = not turn

        move(turn)
        display_field()


game()
