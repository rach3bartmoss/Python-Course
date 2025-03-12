undead = {	'hp': 100,
			'stamina': 80,
			'dmg': 15,
			'armor': 40,
			'name': "The Chosen Undead"
}

x = undead.items() #the items() method returns a view object, the objects contains a key-value pairs
#of the dictionary, as TUPLES in a LIST
undead['hp'] = 90
print(x)
#https://www.w3schools.com/python/python_ref_dictionary.asp --references for dictionary methods

#ITEMS() RETURNS A LIST OF TUPLES
#KEYS() RETURNS A LIST
for key, value in undead.items():
	print(f"Key:{key}")
	print(f"{value}")
