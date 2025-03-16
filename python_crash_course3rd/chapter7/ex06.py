pool = dict()

print("Please enter your name and your dream vacation!")
while True:
	name = input("Your name: ")
	if name.lower() == 'exit':
		break
	local = input("The dream spot: ")
	pool[name] = local

for person, spot in pool.items():
	print(f"{person.title()} dream vacation is at {spot.title()}!")