def common(lst1, lst2): 
    return list(set(lst1) & set(lst2))[0]


with open('puzzle_input.txt') as file:
    puzzle_input = file.read().splitlines()
    
total = 0
    
for line in puzzle_input:
    half_length = len(line) // 2
    item1, item2 = line[:half_length], line[half_length:]
    
    common_item = common(item1, item2)
    total += ord(common_item) - 38 if common_item.isupper() else ord(common_item) - 96
    
print(total)
