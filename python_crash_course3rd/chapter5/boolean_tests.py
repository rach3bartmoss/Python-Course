
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("Is car == 'audi'? I predict False.")
print(car == 'audi')

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.append('HONDA')
print(cars)

car = 'honda'

print(car.upper() in cars)
print(car not in cars)

for brand in cars:
	if brand.lower() == 'bmw':
		print("BAYERISCHE MOTOREN WERKE MENTIONED!!!!")
	print('bmw' in brand)

print("\nnumbers:")
print(42 > 2077)
print(42 < 2077)
print(42 == 2077)
