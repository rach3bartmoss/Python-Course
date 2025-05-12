import plotly.express as px
import numpy as np
from random_walk import RandomWalk

rw = RandomWalk(150) #to use petal_lenght this is the maximum size, 150
rw.fill_walk()

df = px.data.iris()
fig = px.scatter(df, rw.x_values, rw.y_values, color='petal_length')
fig.show()