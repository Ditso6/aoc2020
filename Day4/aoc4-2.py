def opdracht1():
    print("Antwoord op de eerste vraag: ") 
    check_passports(create_passports(read_input(file)))

def opdracht2():
    print("Antwoord op de tweede vraag: ")
    validate_passports(create_passports(read_input(file)))

def read_input(file):
    with open(file) as f:
        batch = f.read()
    lines = batch.split("\n\n")
    
    blobs = []
    for line in lines:
        blobs.append(line.replace("\n", " "))
    return blobs

def create_passports(blobs):
    passports = []
    for blob in blobs:
        passport = {}
        blob = blob.split()
        for stukjevanblob in blob:
            key, value = stukjevanblob.split(":")
            passport[key] = value
        passports.append(passport)
    return passports

def check_passports(passports):
    complete_passports = 0
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for passport in passports:
        passport_required_fields = 0
        for field in required_fields:
            if field in passport:
                passport_required_fields += 1
        if passport_required_fields == 7:
            complete_passports += 1
    print(complete_passports)

def validate_passports(passports):
    validpassports = 0
    for passport in passports:
        validation = 0
        if "byr" in passport and len(passport["byr"]) == 4 and 1920 <= int(passport["byr"]) <= 2002:
            validation += 1
        if "iyr" in passport and len(passport["iyr"]) == 4 and 2010 <= int(passport["iyr"]) <= 2020:
            validation += 1
        if "eyr" in passport and len(passport["eyr"]) == 4 and 2020 <= int(passport["eyr"]) <= 2030:
            validation += 1
        if "hgt" in passport:
            if "cm" in passport["hgt"] and 150 <= int(passport["hgt"][:-2]) <= 193:
                validation += 1
            if "in" in passport["hgt"] and 59 <= int(passport["hgt"][:-2]) <= 76:
                validation += 1
        if "hcl" in passport and len(passport["hcl"]) == 7 and all(char in "#abcdef1234567890" for char in passport["hcl"]):
            validation += 1
        if "ecl" in passport and passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            validation += 1
        if "pid" in passport and len(passport["pid"]) == 9 and all(char.isdigit() for char in passport["pid"]):
            validation += 1
        if validation == 7:
            validpassports += 1
    print(validpassports)

while True:
    file = "input.txt"
    opdracht1()
    opdracht2()
    break