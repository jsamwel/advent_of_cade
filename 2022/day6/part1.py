with open('puzzle_input.txt') as file:
    puzzle_input = file.read()
    
start_indexes = []

for index in range(len(puzzle_input)):
    sequence = puzzle_input[index-4:index]
    
    if len(sequence) == 0:
        continue
    
    if len(set(sequence)) == len(sequence):
        start_indexes.append(index)

print(puzzle_input[start_indexes[0]-4:start_indexes[0]], start_indexes[0])
