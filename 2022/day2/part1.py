from enum import IntEnum


"""
Rock A, X
Paper B, Y
Scissors C, Z
"""


class RespondShape(IntEnum):
    X = 1
    Y = 2
    Z = 3
    

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
    
    diff = RespondShape[play[1]] - InputShape[play[0]]
    
    if diff == 0:
        score = 3
    elif diff == 1 or diff == -2:
        score = 6
    else:
        score = 0
    
    total += score + RespondShape[play[1]]
    
print(total)