import dash
from dash.dependencies import Input, Output
from dash import dcc, html
import pandas as pd
from dash import dash_table

# Sample DataFrame
data = {
    'Name': ['Alice', 'Alice Bob', 'Charlie Alice', 'David Alice', ' Alice Eva'],
    'Age': [25, 30, 35, 28, 22],
    'Gender': ['Female', 'Male', 'Male', 'Male', 'Female'],
'City': ['and', 'ang', 'ane', 'ame', 'ame'],
'Gender': ['Female', 'Male', 'Male', 'Male', 'Female']
}
df = pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    html.H1("DataFrame Filter App"),

    # Input component for filtering
    dcc.Input(id='filter-input', type='text', placeholder='Search...'),

    # Output component to display filtered DataFrame
    dash_table.DataTable(
        id='filtered-data',
        columns=[{'name': col, 'id': col} for col in df.columns],
        style_table={'height': '300px', 'overflowY': 'auto'},
        sort_action="native",  # Enable native sorting
        sort_mode="multi"  # Allow multi-column sorting
    ),
])


# Define callback to update the filtered DataFrame
@app.callback(
    Output('filtered-data', 'data'),
    Input('filter-input', 'value'),
    Input('filtered-data', 'sort_by')
)
def update_filtered_data(filter_value, sort_by):
    filtered_df = df
    if filter_value:
        search_terms = filter_value.lower().split()
        for term in search_terms:
            filtered_df = filtered_df[
                filtered_df.apply(lambda row: any(str(val).lower().find(term) != -1 for val in row), axis=1)]

    # Apply sorting
    if sort_by:
        for sort in sort_by:
            filtered_df = filtered_df.sort_values(
                by=sort['column_id'],
                ascending=sort['direction'] == 'asc',
                inplace=False
            )

    return filtered_df.to_dict('records')


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)