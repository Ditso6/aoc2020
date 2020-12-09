file = "input.txt"

with open(file) as f:
	data = f.read().splitlines()

xmasdata = [int(line) for line in data]

answer1 = 0
for i in range(25, len(xmasdata)):
	preamble = xmasdata[i-25: i]
	if not any(nbr1 != nbr2 and nbr1 + nbr2 == xmasdata[i] for nbr1 in preamble for nbr2 in preamble):
		answer1 = xmasdata[i]
		break

print(answer1)

answer2 = 0
for i in range(len(xmasdata)):
	for x in range(i):
		contiguous_set = xmasdata[x:i]
		contiguous_set_sum = sum(contiguous_set)
		if contiguous_set_sum < answer1:
			break
		elif contiguous_set_sum == answer1:
			answer2 = min(contiguous_set) + max(contiguous_set)
	if answer2:
		break

print(answer2)