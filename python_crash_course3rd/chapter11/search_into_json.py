from pathlib import Path
import json

pathtoread = Path(input("Insert the file name: "))

needle = input("Insert the key value to read: ")

try:
	data = pathtoread.read_text()
	dataVer = json.loads(data)
	print(f"Target: {needle}\nCause of death: {dataVer.get(needle)}")
except FileNotFoundError:
	print("File not found")
except Exception as err:
	print(f"Some error occurred: {err}")
