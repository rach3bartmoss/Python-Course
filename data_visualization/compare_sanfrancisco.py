import matplotlib.pyplot as plt
import csv
import matplotlib.dates as mdates
from pathlib import Path
from datetime import datetime

path_sf = Path('weather_data/san_francisco.csv')

lines_sf = path_sf.read_text().splitlines()

reader_sf = csv.reader(lines_sf)
header_sf = next(reader_sf)

highs, lows, dates = [], [], []

for row in reader_sf:
	low = int(row[6])
	high = int(row[5])
	curr_date = datetime.strptime(row[2], '%Y-%m-%d')
	lows.append(low)
	highs.append(high)
	dates.append(curr_date)

fig, ax = plt.subplots(figsize=(15, 6))

ax.plot(dates, highs, color='red')
ax.plot(dates, lows, color='blue')
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Temperatures(F)', fontsize=16)
ax.fill_between(dates, highs, lows, facecolor='red', alpha=0.1)
fig.autofmt_xdate()

ax.xaxis.set_major_locator(mdates.MonthLocator())

plt.show()
