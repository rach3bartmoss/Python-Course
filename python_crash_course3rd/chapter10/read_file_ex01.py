from pathlib import Path

var = Path('learningPython.txt')

content = var.read_text()

var2 = content.replace('python', 'PYTHON')

#lines = content.splitlines() THIS CAN BE SKIPPED SIMPLIFYING THE CODE

print(var)
#print(content)
#print(var2)

print("\n")
for line in content.splitlines():
	print(f"<{line}>")
