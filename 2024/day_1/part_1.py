with open('input.txt') as f:
	lines = f.readlines()

total = 0

for line in lines:
	first = None
	last = None

	for index, item in enumerate(line):
		number = None

		if item.isdigit():
			number = int(item)

			if first is None:
				first = number

			last = number

	total += first * 10 + last

print(total)
