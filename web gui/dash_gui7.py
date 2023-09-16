from dash import Dash, html, dcc, Input, Output
from dash.dependencies import State  # Import State from dash.dependencies
import pandas as pd
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

file_path = 'E://REVA//Healthcare Providers Data For Anomaly Detection//Medicare1//2021_CA_stats_90095.xlsx'
sheet_name = 'data1'

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path, sheet_name=sheet_name,header=0)

# address
# Limit the DataFrame to the first 1000 rows
df = df.head(1000)

# Assuming you have a DataFrame 'df'
# Select the columns you want to keep
selected_columns = ['Rndrng_NPI',
'Rndrng_Prvdr_Last_Org_Name',
'Rndrng_Prvdr_First_Name',
'Rndrng_Prvdr_MI',
'Rndrng_Prvdr_Crdntls',
'Rndrng_Prvdr_Gndr',
'Rndrng_Prvdr_Ent_Cd',
'Rndrng_Prvdr_St1',
'Rndrng_Prvdr_St2',
'Rndrng_Prvdr_City',
'Rndrng_Prvdr_State_Abrvtn',
'Rndrng_Prvdr_State_FIPS',
'Rndrng_Prvdr_Zip5',
'Rndrng_Prvdr_RUCA',
'Rndrng_Prvdr_RUCA_Desc',
'Rndrng_Prvdr_Cntry'
]

# Use the selected columns to create a new DataFrame
address_filtered_df = df[selected_columns]

# Remove duplicate rows based on the selected columns
address_filtered_df = address_filtered_df.drop_duplicates()

# Store the last 10 search results
last_10_search_results = []

app.layout = html.Div([
    html.Div([
        dcc.Input(id='search-bar', type='text', placeholder='Search...'),
        html.Button('Search', id='search-button'),
    ]),

    html.Div([
        dcc.Dropdown(id='last-searches-dropdown', options=[], placeholder='Select a previous search...'),
    ]),

    html.Div([
        dcc.Graph(
            id='search-results',
            config={'scrollZoom': False}
        ),
    ]),
])


@app.callback(
    Output('search-results', 'figure'),
    Output('last-searches-dropdown', 'options'),
    Input('search-button', 'n_clicks'),
    Input('last-searches-dropdown', 'value'),
    State('search-bar', 'value'),
)
def update_search_results(n_clicks, selected_search, search_query):
    global last_10_search_results

    if n_clicks:
        # Perform search in the DataFrame
        filtered_df = df[df.apply(lambda row: any(search_query.lower() in str(row[col]).lower() for col in address_filtered_df.columns), axis=1)]

        # Store the search result
        last_10_search_results.insert(0, filtered_df.head(10))

        # Keep only the last 10 search results
        last_10_search_results = last_10_search_results[:10]

    if selected_search is not None:
        # Show the selected search result
        selected_result = last_10_search_results[selected_search]
        fig = px.scatter(selected_result, x='Country Name', y='Value', text='Indicator Name')
        fig.update_traces(textposition='top center')
        return fig, dash.no_update

    return px.scatter(), [{'label': i, 'value': idx} for idx, i in enumerate(last_10_search_results)]


if __name__ == '__main__':
    app.run(debug=True)
