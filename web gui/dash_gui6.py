import dash
from dash import html
from dash.dependencies import Input, Output
from dash import dash_table
import dash_bootstrap_components as dbc
import pandas as pd
from dash import dcc

# Replace 'your_file.xlsx' with the path to your Excel file and 'your_sheet_name' with the actual sheet name.
file_path = 'E://REVA//Healthcare Providers Data For Anomaly Detection//Medicare1//2021_CA_stats_90095.xlsx'
sheet_name = 'data1'

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path, sheet_name=sheet_name,header=0)

# Limit the DataFrame to the first 1000 rows
df = df.head(1000)

# # Sample DataFrame for demonstration
# data = {
#     'Name': ['Alice', 'Alice Bob', 'Charlie Alice', 'David Alice', ' Alice Eva'],
#     'Age': [25, 30, 35, 28, 22],
#     'Gender': ['Female', 'Male', 'Male', 'Male', 'Female'],
#     'City': ['and', 'ang', 'ane', 'ame', 'ame'],
#     'Gender': ['Female', 'Male', 'Male', 'Male', 'Female']
# }
#
# df = pd.DataFrame(data)

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
