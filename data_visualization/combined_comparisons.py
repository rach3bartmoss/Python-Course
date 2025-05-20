import matplotlib.pyplot as plt
from pathlib import Path
import csv
import matplotlib.dates as mdates
from datetime import datetime

def	get_index(header_row: list, target_value: str) -> int:
	index = 0
	for head in header_row:
		if head == target_value:
			break
		index += 1
	return index

path_death = Path('weather_data/death_valley_2021_full.csv')
path_sitka = Path('weather_data/sitka_weather_2021_full.csv')
path_sf = Path('weather_data/san_francisco.csv')

lines_sf = path_sf.read_text().splitlines()
lines_dv = path_death.read_text().splitlines()
lines_sv = path_sf.read_text().splitlines()

reader_sf = csv.reader(lines_sf)
reader_dv = csv.reader(lines_dv)
reader_sv = csv.reader(lines_sv)

header_sf, header_dv, header_sv = next(reader_sf), next(reader_dv), next(reader_sv)

print(f"{header_sf} -> type {type(header_sf)}")

tmax_index = get_index(header_sf, 'TMAX')
tmin_index = get_index(header_sf, 'TMIN')
date_index = get_index(header_sf, 'DATE')
name_index = get_index(header_sf, 'NAME')

highs_sf, lows_sf, dates_sf = [], [], []
title = ''

for row in reader_sf:
	high = int(row[tmax_index])
	low = int(row[tmin_index])
	date = datetime.strptime(row[date_index], '%Y-%m-%d')
	highs_sf.append(high)
	lows_sf.append(low)
	dates_sf.append(date)
	title = str(row[name_index])

fig, ax = plt.subplots(figsize=(15, 6))

ax.plot(dates_sf, highs_sf, color='red')
ax.plot(dates_sf, lows_sf, color='blue')

ax.set_title(title, fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Temperatures(F)', fontsize=16)
fig.autofmt_xdate()
ax.tick_params(labelsize=12)

ax.xaxis.set_major_locator(mdates.MonthLocator())

plt.show()
