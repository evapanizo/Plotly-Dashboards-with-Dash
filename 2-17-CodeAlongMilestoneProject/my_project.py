# Libraries
import dash
import pandas as pd
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt
from datetime import timedelta as td
from dash.dependencies import Input, Output, State

# Read data
path = "/Users/eva/Documents/Cursos/Dash-Udemy/exercises/2-17-CodeAlongMilestoneProject/data/companydata.csv"
data = pd.read_csv(path).T

# Data Wrangling
data.columns = data.loc['0', :]
data.drop('0', inplace=True)
data.reset_index(drop=True, inplace=True)
dates_dict = {days: (dt.today() - td(days=days)).strftime("%Y-%m-%d") for days in range(len(data.index))}
data.rename(index=dates_dict, inplace=True)

# Useful variables
min_date = dt.strptime(data.index[-1], "%Y-%m-%d")
max_date = dt.strptime(data.index[0], "%Y-%m-%d") + td(days=1)

# Companies
companies_list = data.columns.sort_values()

# Create Dash app
app = dash.Dash()

# Layout
app.layout = html.Div([
    
    html.H1("Stock Ticker Dashboard"),

    html.Div(id="control-panel", children = [
        html.Div(id="symbol-selector", children = [
            html.H3("Select stock symbols:"),
            dcc.Dropdown(id="dropdown", 
                        options=[{"label": company, "value": company} for company in companies_list],
                        multi=True,
                        value=[companies_list[0]],
            )
        ]),

        html.Div(id="date-selector", children = [
            html.H3("Select start and end dates:"),
            dcc.DatePickerRange(id='date-picker-range',
                                start_date=min_date,
                                end_date=dt.today(),
                                min_date_allowed=min_date, 
                                max_date_allowed=dt.today(),
                                display_format = "YYYY-MM-DD"
            )
        ]),

        html.Div(id="submit-container", children = [
            html.Button('Submit', id='button')
        ])

    ]),

    html.Div(id="graph-container", children=[
        dcc.Graph(id="stock-time-series")
    ])

])

@app.callback(Output("stock-time-series", "figure"), 
             [Input("button", "n_clicks")], 
             [State("dropdown", "value"), 
              State("date-picker-range", "start_date"),
              State("date-picker-range", "end_date")])
def update_time_series(n_clicks, companies, start, end):
    start = dt.strptime(start[0:10], "%Y-%m-%d")
    end = dt.strptime(end[0:10], "%Y-%m-%d")
    dates = [(start + td(days=days)).strftime("%Y-%m-%d") for days in range((end-start).days + 1)]
    filtered_data = data.loc[dates, companies]
    traces = [go.Scatter(x=filtered_data.index, y=filtered_data[company], mode="lines", name=company) for company in companies]
    return {"data": traces, 
            "layout": go.Layout(title="Closing Prices",
                                xaxis=dict(type="date", range=(start, end), tickformat="%d %B %Y"))}

# Run Dash app
if __name__ == "__main__":
    app.run_server()