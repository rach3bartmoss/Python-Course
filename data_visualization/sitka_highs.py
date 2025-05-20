from pathlib import Path
import matplotlib.pyplot as plt
from datetime import datetime
import csv

path = Path('weather_data/sitka_weather_2021_simple.csv')

lines = path.read_text().splitlines()
"""
	read_text() reads the contents into the 'lines' variable as a str
	splitlines() will create a list of string from 'lines' newline as delimiter
"""

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

dates, highs, lows = [], [], []

for row in reader:
	high = int(row[4])
	low = int(row[5])
	date = datetime.strptime(row[2], '%Y-%m-%d')
	highs.append(high)
	dates.append(date)
	lows.append(low)

fig, ax = plt.subplots(figsize=(15, 6))
#fig, bx = plt.subplots(figsize=(15, 6)) #creates a new map window
# figplt, ax = plt.subplots(nrows=2, ncols=1, figsize=(15, 10)) ##creates one window with two or more plots array-like

ax.plot(dates, highs, color='red', linewidth=1, alpha=0.5)
ax.plot(dates, lows, color='blue', linewidth=1, alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='gray', alpha=0.1)

ax.set_title("Daily High Temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate() #this call draws the dates diagonally to prevent overlapping
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=12)



plt.show()
