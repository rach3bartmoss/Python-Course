utente1 = {
	'specie': 'dog',
	'pet_name': 'churros',
	'race_type': 'malinois',
	'owner_name': 'frank ocean',
}

utente2 = {
	'specie': 'cat',
	'pet_name': 'baba gato',
	'race_type': 'british short hair',
	'owner_name': 'wiz khalifa',
}

utente3 = {
	'specie': 'snake',
	'pet_name': 'shingashana',
	'race_type': 'python',
	'owner_name': 'joe mama',
}

pets = [utente1, utente2, utente3]

for info in pets:
	name = info.get('pet_name')
	print(f"{name.title()}\n")
	for keys, values in info.items():
		print(f"{keys}: {values}")
	
