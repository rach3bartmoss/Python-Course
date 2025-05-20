from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

print(header_row)

dates, lows, highs = [], [], []

for row in reader:
	current_date = datetime.strptime(row[2], '%Y-%m-%d')
	try:
		high = int(row[3])
		low = int(row[4])
	except ValueError:
		print(f"Missing data for {current_date}")
	else:
		dates.append(current_date)
		highs.append(high)
		lows.append(low)

fig, ax = plt.subplots(figsize=(12,6))

ax.plot(dates, highs, color='red')
ax.plot(dates, lows, color='blue')
ax.fill_between(dates, highs, lows, facecolor='yellow', alpha=0.1)
ax.set_title('Daily High and Low Temperatures, 2021\nDeath Valley, CA', fontsize=20)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Temperatures (F)', fontsize=16)
fig.autofmt_xdate()

plt.show()

