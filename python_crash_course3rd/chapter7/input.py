prompt = "wassup my nigga"
prompt += "\nwhats yo name, nigga?"

message = input(prompt)
print(message)

print(input("could this work? "))

number = int(input("enter a number: ")) #can i call this nested in a function argument?
if number % 2 == 0:
	print(f"\nThe number {number} is even.")
else:
	print(f"\nThe number {number} is odd.")