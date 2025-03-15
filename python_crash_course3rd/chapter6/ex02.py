eren = {
	'full_name': "eren yeager",
	'titan': True,
	'affiliate': "exploration corps",
	'birth_place': "paradis",
	'age': 15,
}

mikasa = {
	'full_name': "mikasa ackermann",
	'titan': False,
	'affiliate': "exploration corps",
	'birth_place': "paradis",
	'age': 16,
}

armin = {
	'full_name': "armin leonhardt",
	'titan': True,
	'affiliate': "exploration corps",
	'birth_place': "paradis",
	'age': 15,
}

people = [eren, mikasa, armin]

for person in people:
	info = person.get('full_name')
	print(f"{info.title()} info:\n{person}\n")