undead1 = {	'hp': 100,
			'stamina': 80,
			'dmg': 15,
			'armor': 40,
			'name': "The Chosen Undead"
}

undead2 = {	'hp': 120,
			'stamina': 60,
			'dmg': 10,
			'armor': 50,
			'name': "The Bald Undead"
}

undead3 = {	'hp': 100,
			'stamina': 90,
			'dmg': 25,
			'armor': 25,
			'name': "The Knight Undead"
}

undeads = [undead1, undead2, undead3]

for undead in undeads:
	print(undead)
print("\n")

undeads_army = []
for undead_index in range(20):
	new_undead = undead3.copy()
	undeads_army.append(new_undead)

for undead in undeads_army[:5]:
	print(undead)
print(f"Army lenght: {len(undeads_army)}")
print("\n")

for undead in undeads_army[:3]:
	rankup_undead = undead2.copy()
	undead.update(rankup_undead) #the updated item can be a dictionary or a iteratable object

for undead in undeads_army[:len(undeads_army)]:
	print(undead)
