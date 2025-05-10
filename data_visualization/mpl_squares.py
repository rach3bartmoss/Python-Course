import matplotlib.pyplot as plt
import numpy as np

input_values = [1, 2, 3, 4, 5, 6]
squares = [1, 4, 9, 16, 25, 36]

scatter_values = [(2, 7), (1, 6), (7, 6), (4, 18)]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

"""
	Interpolation usage in numpy method INTERP:
		The simplest form, linear interpolation, connects two known points with a
		straight line and calculates the intermediate values along that line.

		basically what a linear interpolation will do is return a expect Y position
		based on a given X value, and the previous values that draw a line.
"""

for x, y in scatter_values:
	expected_y = np.interp(x, input_values, squares)
	if y > expected_y:
		ax.scatter(x, y, color='green')
	else:
		ax.scatter(x, y, color='red')


ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(labelsize=14)

"""Cursor x, y connection on plot"""
vline = ax.axvline(x=0, color='gray', linestyle='--')
hline = ax.axhline(y=0, color='gray', linestyle='--')

def	on_mouse_move(event):
	if event.xdata is not None and event.xdata is not None and event.ydata is not None:
		x = event.xdata
		y = event.ydata

		vline.set_xdata([x, x])
		hline.set_ydata([y, y])
		fig.canvas.draw_idle()

fig.canvas.mpl_connect("motion_notify_event", on_mouse_move)


plt.show()
