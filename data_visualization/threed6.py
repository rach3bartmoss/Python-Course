from die import Die
import plotly.express as px

die1 = Die()
die2 = Die()
die3 = Die()

"""Some alterations to multiply instead of sum"""

results = []
for rolls in range(100):
	result = die1.roll() * die2.roll()
	#+ die3.roll()
	results.append(result)

frequencies = []
max_result = die1.num_sides * die2.num_sides
#* die3.num_sides
poss_results = range(1, max_result + 1)
for value in poss_results:
	frequency = results.count(value)
	frequencies.append(frequency)

#labels = {'x': 'Results', 'y': 'Frequency of result'}

#fig = px.bar(x=poss_results, y=frequencies, labels=labels)
fig = px.bar(x=poss_results, y=frequencies)
fig.update_layout(xaxis_dtick=1)

fig.show()
