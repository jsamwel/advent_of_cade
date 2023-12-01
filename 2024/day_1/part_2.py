numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


with open('input.txt') as f:
	lines = f.readlines()

total = 0

for line in lines:
	first = None
	first_index = None
	last = None
	last_index = None

	for index, item in enumerate(line):
		number = None

		if item.isdigit():
			number = int(item)

			if first is None:
				first = number
				first_index = index

			last = number
			last_index = index

	for index, number in enumerate(numbers):
		number_index = line.find(number)

		if number_index != -1 and number_index < first_index:
			first = index + 1
			first_index = number_index

		number_index = line.rfind(number)

		if number_index != -1 and number_index > last_index:
			last = index + 1
			last_index = number_index

	total += first * 10 + last

print(total)
