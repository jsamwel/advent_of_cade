from enum import IntEnum


"""
Rock A, X
Paper B, Y
Scissors C, Z
"""


class PlayResult(IntEnum):
    X = 0
    Y = 3
    Z = 6
    

class InputShape(IntEnum):
    A = 1
    B = 2
    C = 3


with open('puzzle_input.txt') as file:
    puzzle_input = file.read().splitlines()

total = 0

for line in puzzle_input:
    score = 0
    play = line.split(' ')
     
    if PlayResult[play[1]] == 6:
        score = InputShape[play[0]] + 1 if InputShape[play[0]] + 1 < 4 else 1
    elif PlayResult[play[1]] == 3:
        score = InputShape[play[0]]
    else:
        score = InputShape[play[0]] - 1 if InputShape[play[0]] - 1 > 0 else 3
    
    total += score + PlayResult[play[1]]
    
print(total)