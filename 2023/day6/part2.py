with open('puzzle_input.txt') as file:
    puzzle_input = file.read()
    
start_indexes = []
message_length = 14

for index in range(len(puzzle_input)):
    sequence = puzzle_input[index-message_length:index]
    
    if len(sequence) == 0:
        continue
    
    if len(set(sequence)) == len(sequence):
        start_indexes.append(index)

print(puzzle_input[start_indexes[0]-message_length:start_indexes[0]], start_indexes[0])