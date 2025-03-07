import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, html, dash_table, dcc, callback, Output, Input

def main():
    # Incorporate data
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

    # Initialize the app
    app = Dash(__name__)

    # App layout
    app.layout = html.Div([
        html.H1(children='My First App with Data'),
        html.Hr(),
        dcc.RadioItems(
            options=[
                {'label': 'Population', 'value': 'pop'},            #good use of dictinary to rename columns
                {'label': 'Life Expectancy', 'value': 'lifeExp'},
                {'label': 'GDP per Capita', 'value': 'gdpPercap'}
            ],
            value='lifeExp',
            id='controls-and-radio-item'
        ),
        dcc.Graph(
            figure={},
            id='controls-and-graph'
        )
    ])

    # Callbacks
    @callback(
        Output(component_id='controls-and-graph', component_property='figure'),
        Input(component_id='controls-and-radio-item', component_property='value')
    )

    def update_graph(selected_value):
        fig = px.histogram(df, x='continent', y=selected_value, histfunc='avg', title=f'Average {selected_value} by Continent')
        return fig
    # Run the app
    app.run(debug=True)

if __name__ == '__main__':
    main()

