sandwich_orders = list()
finished_sandwiches = list()

print("Enter your sandwiches orders: <write finish to end your order>")

while True:
	curr = input()
	if curr == 'finish':
		break
	sandwich_orders.append(curr)

print(f"Your order:\n{sandwich_orders}")

while sandwich_orders:
	curr = sandwich_orders.pop()
	print(f"Your {curr} sandwich is ready")
	finished_sandwiches.append(curr)

print(sandwich_orders)
print(finished_sandwiches)