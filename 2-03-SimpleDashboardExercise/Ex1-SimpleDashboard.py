#######
# Objective: build a dashboard that imports OldFaithful.csv
# from the data directory, and displays a scatterplot.
# The field names are:
# 'D' = date of recordings in month (in August),
# 'X' = duration of the current eruption in minutes (to nearest 0.1 minute),
# 'Y' = waiting time until the next eruption in minutes (to nearest minute).
######

# Perform imports here:
import dash
import pandas as pd
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html

# Launch the application:
app = dash.Dash()

# Create a DataFrame from the .csv file:
df = pd.read_csv("./Data/OldFaithful.csv")

# Create a Dash layout that contains a Graph component:
data = [go.Scatter(x=df['X'], y=df['Y'], mode="markers", marker=dict(size=12, color="blue"))]
layout = go.Layout(title="Old Faithful Eruption Interval VS Duration",
                   xaxis=dict(title="Eruption duration (minutes)"),
                   yaxis=dict(title="Interval to next eruption (minutes)"),
                   hovermode="closest")

app.layout = html.Div([
    html.H1("My First Simple Dashboard", id="page-header"),
    dcc.Graph(id="first-graph", figure=dict(data=data, layout=layout))
])

if __name__ == "__main__":
    app.run_server()


















# Add the server clause:
