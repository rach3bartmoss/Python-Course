message = input("Which car are you looking for: ")
print(f"We'll se if we have a {message.title()}.")

message = int(input("How many people are in your dinner group? "))

if message > 8:
	print("Sorry you will have to wait for a table.")
elif message <= 8 and message >= 1:
	print("Please come in, we have a table.")

message = int(input("Please enter a number: "))
if message % 10 == 0:
	print(f"{message} is a multiple of 10")
else:
	print(f"{message} is not a multiple of 10")