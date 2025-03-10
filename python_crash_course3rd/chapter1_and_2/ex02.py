import sys

if len(sys.argv) != 3:
	print("usage: python3 ex02.py '<author>' '<quote>'")
	sys.exit(1)

author = sys.argv[1]
quote = sys.argv[2]

message = f"\t{author.title()} once said, \"{quote}.\"\n"

print(message.lstrip())
print(message.rstrip())
print(message.strip())
