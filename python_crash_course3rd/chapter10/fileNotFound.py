from pathlib import Path

def	count_word(path):
	try:
		contents = path.read_text(encoding='utf-8')
	except FileNotFoundError:
		print("Path to file not found")
	else:
		words = contents.split()
		num_words  = len(words)
		return(num_words)

path1 = Path(input('Filename: '))

print(f"Number of words: {count_word(path1)}")
