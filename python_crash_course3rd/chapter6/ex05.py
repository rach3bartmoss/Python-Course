persons = {
	'dorival': [20, 77, 1999],
	'joe mama': [35, 11],
	'rache': [21, 13],
}

for person, numbers in persons.items():
	print(f"{person.title()} favorite numbers are: ", end='')
	for number in numbers:
		print(f"{number}", end=' ')
	
	print('\n')