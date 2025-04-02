#FUNCTION that is part of a class is called a METHOD
from datetime import datetime

class Dog:
	def	__init__(self, name, age):
		self.name = name
		self.age = age

	def	sit(self):
		print(f"{self.name} is sat!")

	def	roll_over(self):
		print(f"{self.name} rolled over!")

	def	yearBirth(self):
		currentYear = datetime.now().year
		print(f"{self.name.title()} year of birth is {currentYear - self.age}!")

myDog = Dog('Billy', 16)
myDog.yearBirth()
myDog.roll_over()
myDog.sit()
