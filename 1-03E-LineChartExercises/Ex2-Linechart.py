#######
# Objective: Using the file 2010YumaAZ.csv, develop a Line Chart
# that plots seven days worth of temperature data on one graph.
# You can use a for loop to assign each day to its own trace.
######

# Perform imports here:
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Create a pandas DataFrame from 2010YumaAZ.csv
df = pd.read_csv('./Data/2010YumaAZ.csv')
days = ['MONDAY', 'TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']

# Use a for loop (or list comprehension to create traces for the data list)
data = []

for day in days:
    # What should go inside this Scatter call?
    filtered_df = df[df['DAY'] == day]
    time = filtered_df['LST_TIME']
    temperature = filtered_df['T_HR_AVG']
    trace = go.Scatter(x=time, y=temperature, mode='lines', name=day) # Method 1
    # trace = dict(x=time, y=temperature, mode='lines', name=day) # Method 2
    data.append(trace)

# Define the layout
layout = go.Layout(title="Mean temperature per day and hour",
                   xaxis= dict(title="Time"),
                   yaxis= dict(title="Mean temperature"))

# Create a fig from data and layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="./1-03E-LineChartExercises/my_solution.html")