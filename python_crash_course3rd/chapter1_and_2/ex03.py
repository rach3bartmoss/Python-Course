import sys

if len(sys.argv) != 2:
	print("usage: python3 ex03.py <filename>")
	sys.exit(1)

filename = sys.argv[1]

print(filename.removesuffix('.py' or '.txt'))
