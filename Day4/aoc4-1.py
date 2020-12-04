file = "input.txt"

with open(file) as f:
	batch = f.read()
passports = []
valid_passports = 0
required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

passports = batch.split("\n\n")

for passport in passports:
	passport_required_fields = 0
	passport = passport.replace("\n", " ")
	for field in required_fields:
		if field in passport:
			passport_required_fields += 1
	if passport_required_fields == 7:
		valid_passports += 1

print(valid_passports)