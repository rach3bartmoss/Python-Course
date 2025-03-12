favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
'frança': 'ruby',
'faith': 'swift'
}

x = favorite_languages.keys() #creates a LIST with the values of the keys
y = favorite_languages.values() #creates a LIST with the keys
z = favorite_languages.items() #creates a LIST of TUPLES
print(z)
print(y)
print(x)

for name in sorted(favorite_languages.keys()): #or keys()
	print(f"{name}, thank you for taking the poll.")

print("\nThe following languages have been mentioned:")
for language in set(y):
	print(language.title())
#set() method return a list of unrepeated target from a list
