age = int(input("Whats your age? "))
if age <= 3:
	print("Free tickets!")
elif age > 3 and age <= 12:
	print("Tickets will cost $10.")
else:
	print("Tickers will cost 15$.")