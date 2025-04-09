from pathlib import Path

lines = list()

try:
	path1 = Path('chapter5/alien.py')#relative path
	if not path1.exists():#.exists() method from pathlib
		raise FileNotFoundError(f"The file {path1} does not exists.")
	contents = path1.read_text()
	lines = contents.splitlines()
	print(contents)
except FileNotFoundError as err:
	print(err)

var1 = float(3.14367)

print(f"{var1:.2f}\n")

for line in lines:
	print(f"/* {line} */")
