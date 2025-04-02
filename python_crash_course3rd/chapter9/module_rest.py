class	Restaurant:
	def	__init__(self, rest_name, cuisine_type):
		self.name = rest_name
		self.cuisine_type = cuisine_type
		self.open = False
		self.number_served = 0

	def	describe_rest(self):
		print(f"The {self.name.title()} is a {self.cuisine_type.capitalize()} Restaurant!")

	def	open_rest(self):
		self.open = True
		print(f"{self.name.title()} is open!")

	def	set_n_served(self, num):
		if num < self.number_served:
			print("Set value less than current value")
			return
		else:
			self.number_served = num

	def	increment_nserved(self, value):
		if value < 0:
			print("Error: Cannot increment with negative values.")
		else:
			self.number_served += value

class	IceCreamStand(Restaurant):
	def	__init__(self, rest_name, cuisine_type):
		super().__init__(rest_name, cuisine_type)
		self.flavors = ['vanilla', 'strawberry', 'napolitan']

	def	show_flavors(self):
		print("We have this flavors:")
		for	flavor in self.flavors:
			print(f"- {flavor.title()}")