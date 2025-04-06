from random import choice, randint
import random
import string

class	Dice:
	def	__init__(self, sides=6):
		self.n_sides = sides
		self.sidelist = list()
		for i in range(1, sides + 1):
			self.sidelist.append(i)
	
	def	roll_dice(self):
		print(choice(self.sidelist))

	def	get_n_sizes(self):
		print(self.sidelist)

class	Lottery:
	def	__init__(self):
		self.numbers = list()
		self.letters = list()

	def	show_ticket(self):
		print(self.numbers)
		print(self.letters)

	def	generate_ticket_numbers(self):
		for i in range(0, 11):
			self.numbers.append(randint(1, 50))
		for _ in range(5):
			self.letters.append(random.choice(string.ascii_uppercase))

	def	static_ticket(self):
		self.numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
		self.letters = ('a', 'b', 'c', 'd', 'e')

	def	create_ticket_bet(self):
		combined_list = self.numbers + self.letters
		ticket_bet = random.sample(combined_list, 4)
		print(f"Your ticket is: {ticket_bet}")
		return ticket_bet



#dice1 = Dice(int(input("Insert number of sides of the dice: ")))

dice1 = Dice(10)

dice1.roll_dice()
dice1.get_n_sizes()

ticket1 = Lottery()

ticket1.static_ticket()
ticket1.show_ticket()

bet = ticket1.create_ticket_bet()

n_times = 0
res = ticket1.create_ticket_bet()
while (True):
	n_times += 1
	if bet == res:
		print(f"It takes {n_times} to get the winning ticket! Your bet: {bet}, the result: {res}")
		break
	res = ticket1.create_ticket_bet()

print(bet)
