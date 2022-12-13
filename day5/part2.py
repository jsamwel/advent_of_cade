with open('puzzle_input.txt') as file:
    puzzle_input = file.read().splitlines()

seperator_index = puzzle_input.index('')
stacks_input, moves = puzzle_input[:seperator_index], puzzle_input[seperator_index + 1:]

stacks = []
number_of_stacks = len(stacks_input[-1].replace(' ', ''))
highest_stack = len(stacks_input) - 1

stacks = []

for stack_index in range(1, number_of_stacks * 4, 4):
    stack = []
    
    for line_index in range(highest_stack - 1, -1, -1):
        line = stacks_input[line_index]
        
        if line[stack_index].isalpha():
            stack.append(line[stack_index])
        
    stacks.append(stack)


for move_raw in moves:
    move = move_raw.replace('move ', '').replace('from ', '').replace('to ', '')
    move_data = move.split(' ')
    
    amount = int(move_data[0])
    source = int(move_data[1]) - 1
    dest = int(move_data[2]) - 1

    move_data = stacks[source][-amount:]
    stacks[source] = stacks[source][:-amount]
    stacks[dest].extend(move_data)
    
for stack in stacks:
        print(stack)
