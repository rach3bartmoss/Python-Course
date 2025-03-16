curr = dict()

print("Fill dict with user inpur: <Type exit to end program>.")

while 'exit' not in curr.keys():
	user_t = input("Enter your user: ")
	if (user_t.lower() == 'exit'):
		break
	pass_wd = int(input("Enter yout password: "))

	curr[user_t] = pass_wd

for user, password in curr.items():
	print(f"User: {user}\tPassword:{password}")