def scan():
	"""input"""
	file = "input.txt"

	with open(file) as f:
		data = f.read()
		boarding_passes = [list(boarding_pass) for boarding_pass in data.splitlines()]

	return boarding_passes

def determine_row(boarding_pass):
	"""determine row"""
	row_min = 0
	row_max = 127
	for character in boarding_pass[:6]:
		middle = (row_max + row_min) // 2
		if character == "F":
			row_max = middle
		else:
			row_min = middle + 1
	if boarding_pass[6] == "F":
		row = row_min
	else:
		row = row_max
	return row

def determine_column(boarding_pass):
	"""determine column"""
	col_min = 0
	col_max = 7
	for character in boarding_pass[7:]:
		middle = (col_max + col_min) // 2
		if character == "L":
			col_max = middle
		else:
			col_min = middle + 1
	if boarding_pass[9] == "L":
		column = col_min
	else:
		column = col_max
	return column

def calculate_seat_ID(row, column):
	"""calculate seat_ID"""
	seat_ID = (row*8)+column
	return seat_ID

def scan_boarding_passes():
	seat_IDs = []
	boarding_passes = scan()

	for boarding_pass in boarding_passes:
		row = determine_row(boarding_pass)
		column = determine_column(boarding_pass)
		seat_ID = calculate_seat_ID(row, column)
		seat_IDs.append(seat_ID)

	return seat_IDs

def find_my_seat():
	seat_IDs = scan_boarding_passes()
	rows = 128
	columns = 8
	available_seats = rows*columns
	possible_seat_IDs = [possible_seat_ID for possible_seat_ID in range(available_seats)]
	for possible_seat_ID in possible_seat_IDs:
		if possible_seat_ID in seat_IDs :
			continue
		if min(seat_IDs) < possible_seat_ID < max(seat_IDs):
			my_seat_ID = possible_seat_ID
			return my_seat_ID

print("Hoogste Seat ID =", max(scan_boarding_passes()))
print("Mijn stoel = seat ID", find_my_seat())