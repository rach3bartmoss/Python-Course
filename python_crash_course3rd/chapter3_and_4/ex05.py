numbers = list(range(0, 37, 11))
print(numbers)

print(min(numbers))
print(max(numbers))
print(sum(numbers))

twenty = list(range(1, 21))
print(twenty)

one_million = list(range(1, 1000001))
#for n in one_million:
	#print(n)
print(min(one_million))
print(max(one_million))
#print(sum(one_million))

twenty = list(range(1, 21, 2))
print(twenty)

threes = []

for i in range(1, 30):
	if i % 3 == 0:
		threes.append(i)
print(threes)

cubes = []
for value in range(1, 11):
	cubes.append(value ** 3)
print(cubes)

comprehension = [value**3 for value in range(1, 11)]
print(comprehension)
