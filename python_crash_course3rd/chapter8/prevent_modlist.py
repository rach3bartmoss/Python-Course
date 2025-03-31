def	print_guest_list(guest_list):
	for guest in guest_list:
		print(f"{guest.title()} has been invited.")

def	modify_guest_list(guest_list):
	present_list = list()
	while guest_list:
		current_guest = guest_list.pop()
		print(f"{current_guest.title()} has arrive at the party!")
		present_list.append(current_guest)
	return present_list


guest_list = list()

guest_list = ['billie eilish', 'rache bartmoss', 'fafe', 'rigby cat', 'neymar jr']

print_guest_list(guest_list)
print("\n")
present_guests = modify_guest_list(guest_list[:]) #the usage [:] is to send a copy

print(guest_list)
print(present_guests)

def	make_pizza(*toppings): #The '*' tells Python to make a tuple called 'toppings', to store all the values the function receives
	print("Ingredients of pizza")
	for topping in toppings:
		print(f"- {topping}")

make_pizza("atum")
make_pizza("atum", "isire", "bacon")

def make_pizza_wsize(size, *toppings): #mixed between positional and arbitrary arguments
	print(f"\nMaking a {size}-inch pizza with the following toppings:")
	for topping in toppings:
		print(f"- {topping}")

def	build_character(name, type, **info): ##using '**' is like to adding a dict element to it
	info['char_name'] = name.title()
	info['char_type'] = type.title()
	return (info)

character = build_character('the chosen', 'undead',
							health_bar=100,
							armor=40)

print(type(character))
print(character)
