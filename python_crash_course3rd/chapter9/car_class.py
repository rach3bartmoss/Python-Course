class	Battery: ##COMPOSITION
	def	__init__(self, battery_size=40):
		self.battery_size = battery_size
		self.battery_autonomy = 350

	def	describe_battery(self):
		print(f"This car has a {self.battery_size}-kWh Battery.")

	def	get_autonomy(self):
		if self.battery_size == 40:
			self.battery_autonomy = 350
		elif self.battery_size == 65:
			self.battery_autonomy = 500
		print(f"Autonomy of {self.battery_autonomy}Kms.")

	def	upgrade_battery(self):
		if self.battery_size == 65:
			print("Car battery already upgraded.")
			return
		elif self.battery_size == 40:
			self.battery_size = 65
			print("Batery upgraded from 40kWh to 65kWh.")

class	Car:
	def	__init__(self, manufacturer, model, year):
		self.manufacturer = manufacturer
		self.model = model
		self.year = year

	def	describe_car(self):
		print("Car description: ")
		print(f"Manufacturer: {self.manufacturer}")
		print(f"Model: {self.model}")
		print(f"Year: {self.year}")

class	ElectricCar(Car):
	def	__init__(self, manufacturer, model, year):
		super().__init__(manufacturer, model, year)
		self.battery = Battery()

renault_9 = ElectricCar('renault', '9', '2077')

renault_9.battery.describe_battery()
renault_9.battery.get_autonomy()

renault_9.battery.upgrade_battery()

renault_9.battery.describe_battery()
renault_9.battery.get_autonomy()