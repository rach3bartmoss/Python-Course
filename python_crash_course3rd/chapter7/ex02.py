message = ""
print("Enter your toppings: ")
while message != 'exit':
	message = input("")
	if (message == 'exit'):
		break
	else:
		print(f"{message.title()} added to the pizza.")