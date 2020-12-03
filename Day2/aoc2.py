with open("Passwords.txt", "r") as f:
	passwords = f.read()

answer1 = answer2 = 0

for line in passwords.splitlines():
	nbrs, letter, pwd = line.split()
	letter = letter.rstrip(":")
	minimum, maximum = nbrs.split("-")
	minimum = int(minimum)
	maximum = int(maximum)
	if minimum <= pwd.count(letter) <= maximum:
		answer1 += 1
	if (pwd[minimum - 1] + pwd[maximum - 1]).count(letter) == 1:
		answer2 +=1

print("Answer 1: ", answer1)
print("Answer 2: ", answer2)