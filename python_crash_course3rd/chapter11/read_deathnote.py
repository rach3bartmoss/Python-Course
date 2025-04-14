from pathlib import Path
import json

pathname = Path(input("Insert the .json file to read: "))

dataList = pathname.read_text()
contents = json.loads(dataList)

for content in contents.items():
	print(content)
