class	User:
	def	__init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = 0

	def	describe_user(self):
		print(f"{self.first_name} {self.last_name}")
		print(self.login_attempts)

	def	increment_login_attempts(self):
		self.login_attempts += 1

	def	reset_login_attempts(self):
		self.login_attempts = 0

#applying inheritance
#  parent class is also known as superclass
#  child class is also known as subclass

class UserGuest(User):#CHILD CLASS FROM PARENT CLASS (USER)
	def	__init__(self, first_name, last_name):
		super().__init__(first_name, last_name)
		self.battery = Battery()##COMPOSITION


class	Privileges:
	def	__init__(self):
		self.privileges = ['read', 'write', 'rwrite', 'add', 'remove', 'ban']
	def	show_privileges(self):
		print("Privileges of current user: ")
		for privilege in self.privileges:
			print(f"- {privilege}")

class	Admin(User):
	def	__init__(self, first_name, last_name):
		super().__init__(first_name, last_name)
		self.privileges = Privileges()

admin1 = Admin('sudo', 'rache')
admin1.describe_user()
admin1.privileges.show_privileges()

guest1 = UserGuest('convidado', '001')
guest1.describe_user()