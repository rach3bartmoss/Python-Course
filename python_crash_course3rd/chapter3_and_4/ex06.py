#slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:5])
print(players[2:])
print(players[-3:])

print("\nHere are the first three players on my team:")
for player in players[:3]:
	print(player.title())
