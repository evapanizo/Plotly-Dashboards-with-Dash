#######
# Objective: Using the "flights" dataset available
# from the data folder as flights.csv
# create a heatmap with the following parameters:
# x-axis="year"
# y-axis="month"
# z-axis(color)="passengers"
######

# Perform imports here:
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objects as go

# Create a DataFrame from  "flights" data
df = pd.read_csv('./Data/flights.csv')

# Define a data variable
data = [go.Heatmap(x=df['year'], y=df['month'], z=df['passengers'].values.tolist(), 
                   colorscale='Jet', colorbar=dict(title="Passengers"))]

# Define the layout
layout = go.Layout(title="Flights Heatmap")

# Create a fig from data and layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="./1-09E-HeatmapExercises/my_solution.html")