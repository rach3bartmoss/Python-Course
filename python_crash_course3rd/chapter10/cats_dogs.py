from pathlib import Path

try:
	dogs = Path('dogs.txt')
	cats = Path('cats.txt')

	try:
		content1 = dogs.read_text()
	except FileNotFoundError:
		print(f"File {dogs} not found")
	else:
		print(content1)
	try:
		content2 = cats.read_text()
	except FileNotFoundError:
		print(f"File {cats} not found")
	else:
		print(content2)
except:
	pass
