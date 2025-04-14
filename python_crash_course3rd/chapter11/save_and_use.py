from pathlib import Path
import json

target = input("Who you gonna kill? ")
while target.strip() == "":
	print("No one huh? Try again")
	target = input("Who you gonna kill? ")

wod = input("How? ")
if wod.strip() == "":
	wod = "Heart Attack."

kill_dict = {target: wod}

path1 = Path('deathnote.json')
try:
	if path1.exists():
		prevData = path1.read_text()
		prevDataCopy = json.loads(prevData)
		mergedDict = prevDataCopy | kill_dict
	else:
		mergedDict = kill_dict
	print(mergedDict)
	path1.write_text(json.dumps(mergedDict, indent=4))
except FileNotFoundError:
	pass
