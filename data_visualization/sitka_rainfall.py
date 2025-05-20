import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import csv
from pathlib import Path
from datetime import datetime

path = Path('weather_data/sitka_weather_2021_full.csv')

lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

dates, daily_rainfall_amounts = [], []

for row in reader:
	rf_amount = float(row[5])
	data = datetime.strptime(row[2], '%Y-%m-%d')
	dates.append(data)
	daily_rainfall_amounts.append(rf_amount)

fig, ax = plt.subplots(figsize=(15, 6))
ax.plot(dates, daily_rainfall_amounts, color='blue')

ax.set_title("Daily Rainfall Amounts, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Daily Amount", fontsize=16)
ax.tick_params(labelsize=12)

ax.xaxis.set_major_locator(mdates.MonthLocator())

plt.show()
