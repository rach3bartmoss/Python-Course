guests = ['ayrton senna', 'dom pedro segundo', 'jesus']

for i in range (0, len(guests)):
	print(f"Hello, {guests[i].title()}, you are invited to my party")

popped_guest = guests.pop(1)
guests.append('jorge ben jor')

print("\n")
for i in range (0, len(guests)):
	print(f"Hello, {guests[i].title()}, you are invited to my party")
print("We found another table for our guests!")

guests.insert(0, 'sasha grey')
guests.insert(2, 'luigi mangioni')
guests.append('rache bartmoss')
print("\n")
for i in range (0, len(guests)):
	print(f"Hello, {guests[i].title()}, you are invited to my party")

print("\nUnfortunually the table will not arrive in time")
for i in range (2, len(guests)):
	print(f"Sorry to uninvite you {guests.pop(2).title()}, but we're full")

print("\n")
for i in range(0, len(guests)):
	print(f"Hello, {guests[i].title()} you are still invited, please come")

i = len(guests)
while i > 0:
	del guests[0]
	i -= 1

print(guests)
