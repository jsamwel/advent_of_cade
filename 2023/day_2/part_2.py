with open('input.txt') as f:
	text = f.read()

lines = text.split('\n')


def find_values(input_set: str):
	color_values = {}

	for color in ['red', 'green', 'blue']:
		index = input_set.find(color)

		if index == -1:
			continue

		color_values[color] = input_set[index - 3:index - 1]

	return color_values


total = 0

for line_index, line in enumerate(lines):
	cube_sets = line.split(';')
	max_values = {}

	for cube_set in cube_sets:
		values = find_values(cube_set)

		for name, value in values.items():
			if (name in max_values and value > max_values[name]) or name not in max_values:
				max_values[name] = value

	power = 1

	for color_value in max_values.values():
		power *= int(color_value)

	total += power

print(total)
