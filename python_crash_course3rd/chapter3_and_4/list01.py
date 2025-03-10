games = ['dark souls 1', 'dark souls 2', 'cyberpunk2077', 'the witcher 3']


for i in range(0, len(games)):
	print(f"My favorite game ever is {games[i].title()}")

print("\n")

cars = ['honda', 'alfa romeo', 'pagani']
print(cars)
cars[2] = 'McLaren'
print(cars)

cars.append('lada')
print(cars)

cars.insert(2, 'vauxhaul')
print(cars)

del cars[2]
print(cars)

print("\n")

popped_cars = cars.pop()
print(cars)
print(popped_cars)

popped_cars = cars.pop(0)
print(popped_cars)

removed = 'alfa romeo'
cars.remove(removed)
print(cars)

print(f"{popped_cars.title()} is too expensive and {removed.title()} is too cheap")
