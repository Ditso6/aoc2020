file = "input.txt"

with open(file) as f:
	batch = f.read()
passports = []
complete_passports = 0
required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

lines = batch.split("\n\n")

for line in lines:
	passports.append(line.replace("\n", " "))

for passport in passports:
	passport_required_fields = 0
	for field in required_fields:
		if field in passport:
			passport_required_fields += 1
	if passport_required_fields == 7:
		complete_passports += 1

print(complete_passports)