#######
# Objective: Make a DataFrame using the Abalone dataset (../data/abalone.csv).
# Take two independent random samples of different sizes from the 'rings' field.
# HINT: np.random.choice(df['rings'],10,replace=False) takes 10 random values
# Use box plots to show that the samples do derive from the same population.
######

# Perform imports here:
import numpy as np
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# create a DataFrame from the .csv file:
df = pd.read_csv("./Data/abalone.csv")

# take two random samples of different sizes:
a_sample = np.random.choice(df['rings'], 60, replace=False)
b_sample = np.random.choice(df['rings'], 50, replace=False)

# create a data variable with two Box plots:
data = [go.Box(y=a_sample, name="A"),
        go.Box(y=b_sample, name="B")]

# add a layout
layout = go.Layout(title="Rings Independent Random Samples")

# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="./1-06E-BoxPlotExercises/my_solution.html")