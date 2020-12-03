file = open('numbers.txt')

input = []
for line in file:
	input.append(int(line))

for num_1 in input:
	for num_2 in input:
		for num_3 in input:
			if num_1 + num_2 + num_3 == 2020:
				print(num_1 * num_2 * num_3)
				exit(0)