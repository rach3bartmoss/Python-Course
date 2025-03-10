import sys
import webbrowser

if len(sys.argv) != 2:
	print("Usage: python remove_prefixes.py <argument>")
	sys.exit(1)

message = sys.argv[1]
formatted_mes = message.removeprefix('https://www.')

print(formatted_mes)

#opens the the url in the default browser of the system
webbrowser.open(f"https://www.{formatted_mes}")
#print(f"DOT:{message}");

#for i in range(1, len(sys.argv)):
	#print(sys.argv[i])
