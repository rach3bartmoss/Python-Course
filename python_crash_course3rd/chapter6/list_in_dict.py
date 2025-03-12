pizza = { #dictionary
	'crust': 'floof', #item
	'toppings': ['parmegiano', 'bacon', 'vitela', 'manjericão'], #list inside a item
	'client_name': "Rache Bartmoss", #another item
}

print(f"You ordered a {pizza['crust']}-crust pizza "
	"with the following toppings:")

for topping in pizza['toppings']:
	print(f"\t{topping}")