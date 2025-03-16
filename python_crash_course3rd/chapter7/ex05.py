sandwich_orders = list()
finished_sandwiches = list()
count = 0

print("Enter your sandwiches orders: <write finish to end your order>")

while count < 3:
	curr = input()
	if curr == 'finish':
		break
	if curr == 'pastrami':
		count += 1
	sandwich_orders.append(curr)

print("We run out pastrami!")

while count > 0:
	sandwich_orders.remove('pastrami')
	count -= 1

print(sandwich_orders)

while sandwich_orders:
	curr = sandwich_orders.pop()
	print(f"Your {curr.title()} sandwich is ready!")
	finished_sandwiches.append(curr)

print(sandwich_orders)
print(finished_sandwiches)