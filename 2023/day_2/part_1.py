with open('input.txt') as f:
	text = f.read()

lines = text.split('\n')

max_values = {
	'red': 12,
	'green': 13,
	'blue': 14
}


def find_values(input_set: str):
	color_values = {}

	for color in ['red', 'green', 'blue']:
		index = input_set.find(color)

		if index == -1:
			continue

		color_values[color] = input_set[index - 3:index - 1]

	return color_values


def check_values(input_values: dict):
	valid_check = True

	for name, value in max_values.items():
		if name in input_values:

			if int(input_values[name]) > value:
				valid_check = False

	return valid_check


total = 0

for line_index, line in enumerate(lines):
	cube_sets = line.split(';')
	color_value = {}

	valid = True

	for cube_set in cube_sets:
		values = find_values(cube_set)

		if not check_values(values):
			valid = False

	if valid:
		total += line_index + 1

print(total)
