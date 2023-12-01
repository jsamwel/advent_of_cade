calories_total = []

with open('puzzle_input.txt') as f:
    input_blob = f.read()
	
elves = input_blob.split('\n\n')

for elf in elves:
    total = 0
    
    for food in elf.split('\n'):
        total += int(food)
        
    calories_total.append(total)
    
print(max(calories_total))