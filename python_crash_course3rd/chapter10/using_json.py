import json
from pathlib import Path

numbers = [2, 7, 45, 51, 77]

path = Path('numbers.json')
contents = json.dumps(numbers)

path.write_text(contents)
