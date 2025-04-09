from pathlib import Path

path1 = Path('guest_book.txt')

content = ""
input_str = ""
print("Please insert the guest list, enter 'exit' to finish")

while (input_str != 'exit'):
	input_str = input()
	if (input_str == 'exit'):
		break
	content += input_str + '\n'
	path1.write_text(content)
