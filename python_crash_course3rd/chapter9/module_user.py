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

class	UserGuest(User):#CHILD CLASS FROM PARENT CLASS (USER)
	def	__init__(self, first_name, last_name):
		super().__init__(first_name, last_name)