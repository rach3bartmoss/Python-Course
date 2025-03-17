def	make_shirt(size, text):
	print(f"size: {size}\ttext: {text}")

def	make_default_shirt(text_t, size='M'):
	print("Ok")

#functions with returned value:
#	strings in python are immutable
#	to modify a string we should convert to a list and then join them again
def	switch_letters(name, letter):
	name_list = list(name)
	print(name_list)
	i = 0
	while i in range(len(name_list)):
		if name_list[i] == letter:
			name_list[i] = 'z'
		i += 1
	return ''.join(name_list)

test = switch_letters('douglas', 's')
print(test)