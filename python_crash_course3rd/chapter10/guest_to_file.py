from pathlib import Path

content = input("Whats you name?\n")

path1 = Path('guest_01.txt')

path1.write_text(content + '\n')
