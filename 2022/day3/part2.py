def common(lst1, lst2, lst3): 
    return list(set(lst1) & set(lst2) & set(lst3))[0]


with open('puzzle_input.txt') as file:
    puzzle_input = file.read().splitlines()
    
total = 0
old_step = 0
groups = []

for step in range(0, len(puzzle_input), 3):
    groups.append(puzzle_input[old_step:step + 3])
    old_step = step + 3
    
for group in groups:
    item = common(*group)
    total += ord(item) - 38 if item.isupper() else ord(item) - 96
    
print(total)