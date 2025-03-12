import time

undead = {	'hp': 100,
			'stamina': 80,
			'dmg': 15,
			'armor': 40,
			'name': "The Chosen Undead"
}

#acessing values in dictionary

print(undead['name'])
print(undead['hp'])
print(undead)

#adding a value to the dictionary
undead['cursed'] = True
print(undead)

if (undead['cursed'] == True):
	time.sleep(0.5)
	print("Curse is gone")
	undead['cursed'] = False

if undead['armor'] <= 20 and undead['armor'] > 10:
	received_dmg = 10
elif undead['armor'] < 10:
	received_dmg = 20
else:
	received_dmg = 5
undead['hp'] = undead['hp'] - received_dmg
print(f"\n{undead}")

undead['cursed'] = True
if (undead['cursed'] == True):
	del undead['name']

char_name = undead.get('name', 'Nameless')
print(f"\n{char_name}")

print(undead)
