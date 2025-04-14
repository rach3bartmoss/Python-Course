from full_name import formatted_name

def	test_formatted_name():
	format_name = formatted_name('rache', 'charles','bartmoss')
	assert format_name == 'Rache Charles Bartmoss'

def	get_formatted_name_loop():
	while True:
		first = input("Enter first name: ")
		if first == 'q':
			break
		last = input("Enter last name: ")
		if last == 'q':
			break
		format_name = formatted_name(first, last)
		print(format_name)
