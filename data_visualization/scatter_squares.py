import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')

input_values = range(1, 1001)
squares = [x**2 for x in input_values]

fig, ax = plt.subplots()
ax.scatter(input_values, squares, s=10)

ax.set_title("Square Numbers", fontsize=20)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(labelsize=14)

#ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style='sci') #labels on plot axis

#plt.show() #to exibit in a window
plt.savefig('scatter_squares_plot.png', bbox_inches='tight') # to save into a file, filename or a Path object
