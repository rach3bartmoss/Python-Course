# IS THE ELIF THE SAME AS (ELSE IF)???	YES IT IS!
# Why wouldn't leave just else if? I dont know

age = 16
if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
else:
	price = 20
print(f"Your admission cost is ${price}.")
