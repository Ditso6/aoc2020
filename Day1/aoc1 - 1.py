file = open('numbers.txt')

input = []
for line in file:
	input.append(int(line))

for num_1 in input:
	for num_2 in input:
		if num_1 + num_2 == 2020:
			print(num_1 * num_2)
			exit(0)