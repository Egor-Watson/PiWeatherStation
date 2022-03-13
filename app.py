from dash import Dash, html, dcc, Output, Input
import plotly.express as px
import pandas as pd
from layouts import generate_main
# from sensor import Sensor

app = Dash(__name__)

# Make sensor object
# sensor = Sensor()

app.layout = html.Div(children=[
    generate_main()
])

@app.callback(
    Output('current', 'children'),
    Input('reading-val', 'n_clicks'),
)
def update_output(n_clicks):
    # temp = sensor.read_temp()
    temp = 0
    return 'The current temp is: {}'.format(
        temp
    )


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')