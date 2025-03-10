cars = ['bmw', 'audi', 'toyota', 'subaru']
cars_reversed = cars.copy()
cars.sort()
print(f"Original list:{cars_reversed}\n")
print(f"Sort list:{cars}\n")
#cars_reversed.sort(reverse=True)
print(f"Sorted() list:{sorted(cars_reversed)}")

##interesting methods for lists:
#clear()	Removes all the elements from the list
#--->count()	Returns the number of elements with the specified value
#	Return the number of times the value 9 appears int the list:
#	points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
#	x = points.count(9)

#--->extend()	Add the elements of a list (or any iterable), to the end of the current list
#	Add the elements of cars to the fruits list:
#	fruits = ['apple', 'banana', 'cherry']
#	cars = ['Ford', 'BMW', 'Volvo']
#	fruits.extend(cars)

#index()	Returns the index of the first element with the specified value
#	fruits = ['apple', 'banana', 'cherry']

#	x = fruits.index("cherry")
