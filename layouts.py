from dash import html


# Layouts go here

def generate_main():
    return html.Div(
        className='main',
        children=[
            html.H1(
                'Temperature + Humidity in the Room'
            ),
            html.Div(
                id='wrapper',
                children=[
                    html.Div(
                        id='graph-wrapper',
                        children=[
                            # add graph here
                        ]
                    ),
                    html.Div(
                        id='triple-wrapper',
                        children=[
                            html.Div(
                                id='current-wrapper',
                                # current reading div
                                children=[
                                    html.Button('Get reading', id='reading-val', n_clicks=0),
                                    html.Div(
                                        id='current',
                                        children=[
                                            'The current reading is: '
                                        ]
                                    )
                                ]
                            ),
                            html.Div(
                                id='past-wrapper',
                                # past readings
                                children=[
                                    'past readings'
                                ]
                            ),
                            html.Div(
                                id='stats-wrapper',
                                # stats like avg
                                children=[
                                    'stats of readings'
                                ]
                            )
                        ]
                    )
                ]
            )
        ]
    )