def	addCalc(var1, var2):
	try:
		print(f"{int(var1)} + {int(var2)} = {int(var1) + int(var2)}")
	except ValueError:
		print("Both elements must be numbers!")

print("Insert 'quit' to stop program")

while True:
	var1 = input("value one: ")
	if var1 == 'quit':
		print("Program ended")
		exit()
	var2 = input("value two: ")
	if var2 == 'quit':
		print("Program ended")
		exit()
	addCalc(var1, var2)
