#######
# Objective: Create a dashboard that takes in two or more
# input values and returns their product as the output.
######

# Perform imports here:
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

# Launch the application:
app = dash.Dash()

# Create a Dash layout that contains input components
# and at least one output. Assign IDs to each component:
app.layout = html.Div([
    html.H1("The product of two numbers!"),
    html.Div([
        dcc.RangeSlider(
            id='range-slider',
            min=-5,
            max=6,
            step=1,
            value=[-1, 1], 
            marks={num: num for num in range(-5,7)},
        )
    ], style={"padding-top": 40, "padding-left": 150, "padding-right": 150}),
    html.Div(id="show-result", style={"padding-top": 80, "padding-left": 150, "font-size": 30})
])

# Create a Dash callback:
@app.callback(Output("show-result", "children"), 
              [Input("range-slider", "value")])
def compute_product(range_list):
    return f"The result is {range_list[0]*range_list[1]}."

# Add the server clause:
if __name__ == "__main__":
    app.run_server()