#coping a list

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] #or use my_foods.copy()
print("My favorite foods are:")
my_foods.append('feijoada')
my_foods.append('francesinha')
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

print(f"\nThe first three itens in the list are: {my_foods[0:3]}")
print(f"\nThe first three itens in the list are: {my_foods[1:4]}")
print(f"\nThe first three itens in the list are: {my_foods[2:5]}")
