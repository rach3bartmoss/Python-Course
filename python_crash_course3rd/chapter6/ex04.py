favorite_places = {
	'dorival': ['oporto','prague', 'arouca'],
	'joe mama': ['penedo', 'geres', 'viseu'],
	'rache': ['ur', 'bacu', 'etiopia'],
}

for person, place in favorite_places.items():
	print(f"{person.title()} favorite places are: ", end='')
	for local in place:
		print(f"{local.title()}", end=' ')
	print('\n')