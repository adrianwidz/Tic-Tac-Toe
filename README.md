Description

Tic-Tac-Toe game simulator with the ability to play from the beginning (empty field) to the result (win or draw). The program asks the user to enter the cell coordinates, analyzes the move for correctness and shows a field with the changes if everything is ok.

Example

The example below shows how your program should work.
The greater-than symbol followed by space (> ) represents the user input.

    ---------
    |       |
    |       |
    |       |
    ---------
    Enter the coordinates: > 2 2
    ---------
    |       |
    |   X   |
    |       |
    ---------
    Enter the coordinates: > 2 2
    This cell is occupied! Choose another one!
    Enter the coordinates: > two two
    You should enter numbers!
    Enter the coordinates: > 1 4
    Coordinates should be from 1 to 3!
    Enter the coordinates: > 1 3
    ---------
    | O     |
    |   X   |
    |       |
    ---------
    Enter the coordinates: > 3 1
    ---------
    | O     |
    |   X   |
    |     X |
    ---------
    Enter the coordinates: > 1 2
    ---------
    | O     |
    | O X   |
    |     X |
    ---------
    Enter the coordinates: > 1 1
    ---------
    | O     |
    | O X   |
    | X   X |
    ---------
    Enter the coordinates: > 3 2
    ---------
    | O     |
    | O X O |
    | X   X |
    ---------
    Enter the coordinates: > 2 1
    ---------
    | O     |
    | O X O |
    | X X X |
    ---------
    X wins
