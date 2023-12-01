with open('puzzle_input.txt') as file:
    puzzle_input = file.read().splitlines()

total = 0

for line in puzzle_input:
    pairs = [part.split('-') for part in line.split(',')]
    pair1 = [int(pairs[0][0]), int(pairs[0][1])]
    pair2 = [int(pairs[1][0]), int(pairs[1][1])]
    
    if pair2[0] <= pair1[0] <= pair2[1] or pair2[0] <= pair1[1] <= pair2[1]:
        total += 1
    elif pair1[0] <= pair2[0] <= pair1[1] or pair1[0] <= pair2[1] <= pair1[1]:
        total += 1
        
print(total)