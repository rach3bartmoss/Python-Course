import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5, 6]
cubics = [1, 8, 27, 64, 125, 216]

input_values2 = range(1, 5001)
cubics2 = [x**3 for x in input_values2]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
fig, bx = plt.subplots()

ax.set_title("Cubic Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cubic of Value", fontsize=14)

ax.tick_params(labelsize=14)
bx.ticklabel_format(style='plain')

ax.plot(input_values, cubics, linewidth=3)
bx.plot(input_values2, cubics2, linewidth=3)

plt.show()
