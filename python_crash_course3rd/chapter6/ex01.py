favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
'frança': 'ruby',
'faith': 'swift'
}

for keys, values in favorite_languages.items():
	print(f"the key are:{keys.title()}")
	print(f"the value are:{values.title()}\n")

favorite_languages.update({'douglas': 'assembly'})
favorite_languages.update({'ana': 'typescript'})

rivers = {
	'eufrates': 'egypt',
	'são francisco': 'brasil',
	'douro': 'portugal'
}
for river, country in rivers.items():
	print(f"The {river.title()} river is in {country.title()}")

print("\n")
poll = {'faith', 'jen', 'phil'}

for keys in favorite_languages.keys():
	if keys.lower() in poll:
		print(f"{keys} already take the poll")
	else:
		print(f"{keys} did not take the poll")
