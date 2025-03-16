message = ""
active = True #using a flag simplify conditions
while active:
	message = input("(parrot) Tell me something, i repeat:\t\t(enter 'quit' to exit program.)\n")
	if message == 'quit' or message == 'exit':
		break #to me more simplistic just exit the loop
		#active = False
	else:
		print(message)