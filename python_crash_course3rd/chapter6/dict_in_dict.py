enemies = {
	'undead': {
		'hp': 100,
		'stamina': 90,
		'dmg': 25,
		'armor': 25,
		'name': "The Undead Knight"
		},
	'ghost': {
		'hp': 50,
		'stamina': 1,
		'dmg': 80,
		'armor': 1,
		'name': "Abyss Sentinel"
	},
}

for enemy, enemy_info in enemies.items():
	print(f"Enemy type: {enemy.title()}")
	name = f"{enemy_info['name']}"

	print(f"Name: {name.title()}")
	print(f"Wiki: {enemy_info}\n")