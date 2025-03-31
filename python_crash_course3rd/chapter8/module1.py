def	make_pizza(size, *toppings):
	print(f"Making a {size}-inch pizza with the following toppings: ")
	for topping in toppings:
		print(f"- {topping}")

def	create_enemy(name, type, level):
	enemy = dict()
	enemy.update({"name": name})
	enemy.update({"Enemy type": type})
	enemy.update({"level": level})

	print(enemy)

def	printing_models(cars):
	for car in cars:
		print(f"We have a {car} on the list")
