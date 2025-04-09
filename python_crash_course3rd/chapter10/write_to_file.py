from pathlib import Path

path1 = Path('rache.txt')
path2 = Path('pi_digits.txt')

content1 = path1.read_text()
content2 = path2.read_text()


print(content1)

print(path2.write_text('3.141592653589793238462643383279502\n'))

content2 += content1

print(content2)
