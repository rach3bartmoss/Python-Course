from module_user import User, UserGuest

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