def	display_message(message):
	print(f"{message}")

def	fav_book(book):
	print(f"{book.title()}")

display_message(input("WRITE A MESSAGE TO DISPLAY: \n"))
fav_book(input("Whats your favorite book? \n"))

#we can set default values to function as well

"""
def describe_pet(pet_name, animal_type='dog'):
	#Display information about a pet.
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

#describe_pet(pet_name='willie')"""