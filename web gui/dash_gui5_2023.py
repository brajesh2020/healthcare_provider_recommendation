from dash.dash_table.Format import Group
from dash import Dash, html, dcc, Input, Output, callback
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dash_table
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
# df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')
df = pd.read_csv('E://Pycharm//HEALTHCARE PROVIDER FRAUD DETECTION ANALYSIS//country_indicators.csv')


app.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Dropdown(
                options=[{'label': col, 'value': col} for col in df['Indicator Name'].unique()],
                value='Fertility rate, total (births per woman)',
                id='crossfilter-xaxis-column',
            ),
            dcc.RadioItems(
                options=[{'label': item, 'value': item} for item in ['Linear', 'Log']],
                value='Linear',
                id='crossfilter-xaxis-type',
                labelStyle={'display': 'inline-block', 'marginTop': '5px'}
            )
        ], style={'width': '49%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                options=[{'label': col, 'value': col} for col in df['Indicator Name'].unique()],
                value='Life expectancy at birth, total (years)',
                id='crossfilter-yaxis-column'
            ),
            dcc.RadioItems(
                options=[{'label': item, 'value': item} for item in ['Linear', 'Log']],
                value='Linear',
                id='crossfilter-yaxis-type',
                labelStyle={'display': 'inline-block', 'marginTop': '5px'}
            )
        ], style={'width': '49%', 'float': 'right', 'display': 'inline-block'})
    ], style={'padding': '10px 5px'}),

    html.Div([
        dcc.Graph(
            id='crossfilter-indicator-scatter',
            hoverData={'points': [{'customdata': 'Japan'}]}
        )
    ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),

    html.Div([
        dcc.Graph(id='x-time-series'),
        dcc.Graph(id='y-time-series'),
    ], style={'display': 'inline-block', 'width': '49%'}),

    html.Div(dcc.Slider(
        min=df['Year'].min(),
        max=df['Year'].max(),
        step=None,
        id='crossfilter-year--slider',
        value=df['Year'].max(),
        marks={str(year): str(year) for year in df['Year'].unique()}
    ), style={'width': '49%', 'padding': '0px 20px 20px 20px'}),

    # Add the search box and table here
    html.Div([
        dcc.Input(id='search-input', type='text', placeholder='Search...'),
        dash_table.DataTable(
            id='table',
            columns=[{'name': col, 'id': col} for col in df.columns],
            data=df.to_dict('records'),
            sort_action='native'
        )
    ])
])

@callback(
    Output('crossfilter-indicator-scatter', 'figure'),
    Input('crossfilter-xaxis-column', 'value'),
    Input('crossfilter-yaxis-column', 'value'),
    Input('crossfilter-xaxis-type', 'value'),
    Input('crossfilter-yaxis-type', 'value'),
    Input('crossfilter-year--slider', 'value'),
    Input('table', 'data'))  # Listen to changes in the filtered data
def update_graph(xaxis_column_name, yaxis_column_name,
                 xaxis_type, yaxis_type,
                 year_value, table_data):  # Include the filtered data in the callback
    dff = pd.DataFrame(table_data)  # Create a DataFrame from the filtered data
    dff = dff[dff['Year'] == year_value]

    fig = px.scatter(dff,
                     x='Value',  # Use the 'Value' column for x
                     y='Value',  # Use the 'Value' column for y
                     hover_name='Country Name'  # Use 'Country Name' directly
                     )

    fig.update_traces(customdata=dff['Country Name'])  # Use 'Country Name' directly

    fig.update_xaxes(title=xaxis_column_name, type='linear' if xaxis_type == 'Linear' else 'log')

    fig.update_yaxes(title=yaxis_column_name, type='linear' if yaxis_type == 'Linear' else 'log')

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    return fig


def create_time_series(dff, axis_type, title):

    fig = px.scatter(dff, x='Year', y='Value')

    fig.update_traces(mode='lines+markers')

    fig.update_xaxes(showgrid=False)

    fig.update_yaxes(type='linear' if axis_type == 'Linear' else 'log')

    fig.add_annotation(x=0, y=0.85, xanchor='left', yanchor='bottom',
                       xref='paper', yref='paper', showarrow=False, align='left',
                       text=title)

    fig.update_layout(height=225, margin={'l': 20, 'b': 30, 'r': 10, 't': 10})

    return fig

@callback(
    Output('x-time-series', 'figure'),
    Input('crossfilter-indicator-scatter', 'hoverData'),
    Input('crossfilter-xaxis-column', 'value'),
    Input('crossfilter-xaxis-type', 'value'))
def update_y_timeseries(hoverData, xaxis_column_name, axis_type):
    country_name = hoverData['points'][0]['customdata']
    dff = pd.DataFrame(df)  # Create a DataFrame from the original data
    dff = dff[dff['Country Name'] == country_name]
    dff = dff[dff['Indicator Name'] == xaxis_column_name]
    title = '<b>{}</b><br>{}'.format(country_name, xaxis_column_name)
    return create_time_series(dff, axis_type, title)

@callback(
    Output('y-time-series', 'figure'),
    Input('crossfilter-indicator-scatter', 'hoverData'),
    Input('crossfilter-yaxis-column', 'value'),
    Input('crossfilter-yaxis-type', 'value'))
def update_x_timeseries(hoverData, yaxis_column_name, axis_type):
    country_name = hoverData['points'][0]['customdata']
    dff = pd.DataFrame(df)  # Create a DataFrame from the original data
    dff = dff[dff['Country Name'] == country_name]
    dff = dff[dff['Indicator Name'] == yaxis_column_name]
    return create_time_series(dff, axis_type, yaxis_column_name)

@callback(
    Output('table', 'data'),
    Input('search-input', 'value'))
def update_table(search_value):
    if not search_value:
        return df.to_dict('records')  # If search is empty, return all records

    # Split the search input into words
    search_words = search_value.lower().split()

    filtered_data = df.copy()

    for word in search_words:
        filtered_data = filtered_data[filtered_data.apply(lambda row: word in str(row).lower(), axis=1)]

    return filtered_data.to_dict('records')

if __name__ == '__main__':
    app.run_server(debug=True)
