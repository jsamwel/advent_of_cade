import numpy as np


with open('puzzle_input.txt') as file:
    puzzle_input = file.read().splitlines()


map_trees = np.zeros((len(puzzle_input[0]), len(puzzle_input)), dtype=np.int8)


def find_visible(row: list):
    highest = int(row[0])
    locations = [0]
    
    for index, tree in enumerate(row):
        if int(tree) > highest:
            locations.append(index)
            highest = int(tree)
            
    return locations
    
# Find trees horizontal
for index, row in enumerate(puzzle_input):
    trees = find_visible(row)
    trees_reversed = find_visible(list(reversed(row)))
    
    for tree in trees:
        map_trees[index][tree] = 1
        
    for tree in trees_reversed:
        map_trees[index][len(row) - tree - 1] = 1
        
# Find trees vertical
for column in range(len(puzzle_input[0])):
    tree_column = ''.join([row[column] for row in puzzle_input])
    trees = find_visible(tree_column)
    trees_reversed = find_visible(list(reversed(tree_column)))
    
    for tree in trees:
        map_trees[tree][column] = 1
        
    for tree in trees_reversed:
        map_trees[len(tree_column) - tree - 1][column] = 1


visible = np.count_nonzero(map_trees)

print(visible)