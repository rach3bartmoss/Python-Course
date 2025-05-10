from die import Die
import matplotlib.pyplot as plt
import plotly.express as px

die = Die()
die_2 = Die(10)

results = []
for roll_num in range(150000):
	result = die.roll() + die_2.roll()
	results.append(result)

plt.style.use('seaborn-v0_8')

frequencies = []
max_result = die.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)
for value in poss_results:
	frequency = results.count(value)
	frequencies.append(frequency)

title = "Results of Rolling One D6 1,000 times"
labels = {'x': 'Result', 'y': 'Frequencies of result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)

#fig.show()
fig.write_html(f'dice_visual_d{die.num_sides}d{die_2.num_sides}.html')
