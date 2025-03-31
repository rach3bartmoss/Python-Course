from module1 import make_pizza, printing_models
from module1 import create_enemy
from module1 import make_pizza as tubarao #Using <as>(keyword) to Give a Function an Alias
import module1 as m1
import module1


module1.make_pizza(16, 'pepperoni', 'cheese', 'bacon') #import module1
module1.make_pizza(25, 'mushrooms', 'tuna')
module1.make_pizza(31, 'nothing')

make_pizza(16, 'pepperoni', 'cheese', 'bacon')#
make_pizza(31, 'nothing') #from module1 import make_pizza


word = 'rache bartmoss'

print(word[0])
print(word[1])
print(len(word))
print(word[len(word) - 1])

print(word[0:7]) #does not include the last index

print(word[:-4])

findString = word.find('e')
print(findString)


create_enemy("Smough", "Unholy Knight", 50)

tubarao(15, 'ananas', 'camarao', 'siri', 'algas')

m1.create_enemy('zombie dragon', 'undead', 40)

cars = ['honda', 'bmw', 'lexus', 'lada', 'mercedes benz'];
printing_models(cars)
