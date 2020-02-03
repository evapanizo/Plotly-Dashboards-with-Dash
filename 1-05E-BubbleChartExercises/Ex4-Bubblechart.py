#######
# Objective: Create a bubble chart that compares three other features
# from the mpg.csv dataset. Fields include: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'
######

# Perform imports here:
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# create a DataFrame from the .csv file:
df =  pd.read_csv("./Data/mpg.csv")

# create data by choosing fields for x, y and marker size attributes

data = [go.Scatter(x=df['weight'], 
                   y=df['horsepower'],
                   mode='markers',
                   hoverinfo="text",
                   hovertext=[f"Weight: {w}<br>Horsepower: {hp}<br>Acceleration: {acc}<br>Cylinders: {cyl}" 
                              for w, hp, acc, cyl in zip(df['weight'], df['horsepower'], df['acceleration'], df['cylinders'])], 
                   marker=dict(size=df['acceleration'], color=df['cylinders'], 
                               showscale=True, colorbar=dict(title="Cylinders")))]

# create a layout with a title and axis labels
layout = go.Layout(title="Bubble Chart - Weight VS Horsepower", 
                   xaxis=dict(title="Weight"), 
                   yaxis=dict(title="Horsepower"))

# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="./1-05E-BubbleChartExercises/my_solution.html")