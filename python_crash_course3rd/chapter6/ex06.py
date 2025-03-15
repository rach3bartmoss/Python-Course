cities = {
	'natal': {
		'country': 'Brazil',
		'population': 1_000_000,
		'fact': "His natives are also know as Potiguaras, it means shrimp eaters"
	},
	'oporto': {
		'country': 'Portugal',
		'population': 1_000_000,
		'fact': "The city was never conquered, so it got the title of Invicta"
	},
	'romariz': {
		'country': 'Portugal',
		'population': 100_000,
		'fact': "Was originally a roman military camp"
	},
}

for city, info in cities.items():
	print(f"{city.title()}")
	for infos, facts in info.items():
		print(f"{infos}: {facts}", end=', ')
	print('\n')