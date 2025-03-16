unconfirmed_users = ['rache', 'v', 'esdgar', 'ada', 'gauss']
confirmed_users = []

while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print(f"Verifying user: {current_user.title()}")
	confirmed_users.append(current_user)

for confirmed_user in confirmed_users:
	print(confirmed_user.title())

print(unconfirmed_users)
print(confirmed_users)

number_list = [1, 0, 1, 0, 2, 5, 1, 0, 5, 2, 7, 8, 0, 1]

print(number_list)
while 0 in number_list:
	number_list.remove(0)
print(number_list)