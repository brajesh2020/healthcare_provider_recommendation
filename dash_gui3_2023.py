import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import dash_table
import dash_bootstrap_components as dbc

# Sample DataFrame for demonstration
data = {
    'Name': ['Alice', 'Alice Bob', 'Charlie Alice', 'David Alice', ' Alice Eva'],
    'Age': [25, 30, 35, 28, 22],
    'Gender': ['Female', 'Male', 'Male', 'Male', 'Female'],
    'City': ['and', 'ang', 'ane', 'ame', 'ame'],
    'Gender': ['Female', 'Male', 'Male', 'Male', 'Female']
}

df = pd.DataFrame(data)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dbc.Input(id='search-input', type='text', placeholder='Search...'),
    dcc.Graph(id='table-output')
])

@app.callback(
    Output('table-output', 'figure'),
    Input('search-input', 'value')
)
def update_table(search_value):
    if search_value is None:
        return dash_table.DataTable(
            columns=[{'name': col, 'id': col} for col in df.columns],
            data=df.to_dict('records'),
            sort_action='native'
        )
    else:
        filtered_df = df[df.apply(lambda row: any(search_value.lower() in str(cell).lower() for cell in row), axis=1)]
        return dash_table.DataTable(
            columns=[{'name': col, 'id': col} for col in df.columns],
            data=filtered_df.to_dict('records'),
            sort_action='native'
        )

if __name__ == '__main__':
    app.run_server(debug=True)
