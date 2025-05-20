import matplotlib.pyplot as plt
import csv
import matplotlib.dates as mdates
from pathlib import Path
from datetime import datetime

path_death = Path('weather_data/death_valley_2021_full.csv')
path_sitka = Path('weather_data/sitka_weather_2021_full.csv')

lines_death = path_death.read_text().splitlines()
lines_sitka = path_sitka.read_text().splitlines()

reader_d = csv.reader(lines_death)
reader_s = csv.reader(lines_sitka)

header1 = next(reader_d)
header2 = next(reader_s)

highs_d, highs_s = [], []
dates_d, dates_s = [], []

for rowD in reader_d:
	high_d = int(rowD[6])
	curr_dateD = datetime.strptime(rowD[2], '%Y-%m-%d')
	highs_d.append(high_d)
	dates_d.append(curr_dateD)

for rowS in reader_s:
	high_s = int(rowS[7])
	curr_dateS = datetime.strptime(rowS[2], '%Y-%m-%d')
	highs_s.append(high_s)
	dates_s.append(curr_dateS)

fig, ax = plt.subplots(figsize=(15, 6))

ax.plot(dates_d, highs_d, color='blue')
ax.plot(dates_s, highs_s, color='red')
ax.set_title('High Temperatures Comparison Between Sitka Valley and Death Valley, 2021', fontsize=20)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Temperatures(F)', fontsize=16)
fig.autofmt_xdate()
ax.tick_params(labelsize=12)

ax.xaxis.set_major_locator(mdates.MonthLocator())

plt.show()
