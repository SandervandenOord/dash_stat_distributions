# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

from utils import row, column

import numpy as np
from scipy.stats import binom


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': 'white',
    'text': 'blue'
}

app.layout = html.Div(
    children=[
        row([
            html.H2(
                'Visualizing common distributions',
                style={ 'textAlign': 'center', 'color': colors['text']},
        )]),

        row([
            column([
                row([
                    html.Br(),
                    html.Label('Set N:'),
                    dcc.Input(id='set_n', value=10, type='number', min=0, step=1, size=1),
                ]),
                row([
                    html.Label('Set p:'),
                    dcc.Input(id='set_p', value=0.5, type='number', min=0.0, max=1.0, step=0.05),
                ])
            ], className='two columns'),

            column([
                dcc.Graph(
                    id='binomial_graph',
                    config={
                        'displaylogo': False, #dont show plotly logo
                        'modeBarButtonsToRemove': ['pan2d','lasso2d'], #dont show certain options in plotly menu
                    },
                ),
            ], className='eight columns'),
        ]),
    ],
)

@app.callback(
    dash.dependencies.Output('binomial_graph', 'figure'),
    [dash.dependencies.Input('set_n', 'value'), dash.dependencies.Input('set_p', 'value')]
)
def update_figure(set_n, set_p):

    successes = np.arange(0, set_n+1)
    proportions = binom.pmf(successes, set_n, set_p)

    data = {
        'x': successes,
        'y': proportions,
        'type': 'bar',
        'marker': {'color': 'blue'},
    }

    figure = {
         'data': [data],
         'layout': {
             'title': 'Binomial distribution',
             'hovermode': 'closest',
             'plot_bgcolor': colors['background'],
             'paper_bgcolor': colors['background'],
             'font': {
                 'color': colors['text']
             },
             'xaxis': {
                 'title': 'Number of tries',
                 'autotick': False,
             },
             'yaxis': {'title': 'P(X =x)'},
         },
    }
    return figure

if __name__ == '__main__':
    app.run_server(debug=True)