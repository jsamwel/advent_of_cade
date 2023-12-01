import numpy as np


with open('puzzle_input.txt') as file:
    puzzle_input = file.read().splitlines()


rows = []

for row in puzzle_input:
    rows.append([*row])


trees_map = np.array(rows)
trees_scores = np.zeros(np.shape(trees_map), dtype=np.int64)


for index_row, row in enumerate(trees_map):
    for index_column, tree in enumerate(row):
        lookups = []
        list_to_side = [
            np.flip(trees_map[:index_row, index_column]),
            trees_map[index_row + 1:, index_column],
            np.flip(trees_map[index_row, :index_column]),
            trees_map[index_row, index_column + 1:]
        ]

        for side in list_to_side:
            lookups.append(np.where(side>=tree))
        
        score_up = lookups[0][0][0] + 1 if len(lookups[0][0]) > 0 else index_row
        score_down = lookups[1][0][0] + 1 if len(lookups[1][0]) > 0 else np.shape(trees_map)[0] - index_row - 1
        score_left = lookups[2][0][0] + 1 if len(lookups[2][0]) > 0 else index_column
        score_right = lookups[3][0][0] + 1 if len(lookups[3][0]) > 0 else np.shape(trees_map)[1] - index_column - 1
        
        trees_scores[index_row, index_column] = score_left * score_right * score_up * score_down

print(trees_map, '\n\n', trees_scores)
print(np.max(trees_scores), np.where(trees_scores==np.max(trees_scores)))