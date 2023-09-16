import dash
from dash.dependencies import Input, Output
from dash import dcc, html
import pandas as pd
from dash import dash_table
import dash
from dash import html
from dash.dependencies import Input, Output
from dash import dash_table
import dash_bootstrap_components as dbc
import pandas as pd
from dash import dcc

# # Sample DataFrame
# data = {
#     'Name': ['Alice', 'Alice Bob', 'Charlie Alice', 'David Alice', ' Alice Eva'],
#     'Age': [25, 30, 35, 28, 22],
#     'Gender': ['Female', 'Male', 'Male', 'Male', 'Female'],
# 'City': ['and', 'ang', 'ane', 'ame', 'ame'],
# 'Gender': ['Female', 'Male', 'Male', 'Male', 'Female']
# }
# df = pd.DataFrame(data)

# Replace 'your_file.xlsx' with the path to your Excel file and 'your_sheet_name' with the actual sheet name.
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

# Initialize the Dash app
# app = dash.Dash(__name__)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the app layout
app.layout = html.Div([
    html.H1("Healthcare Provider Selector Tool"),

    # Input component for filtering
    dcc.Input(id='filter-input', type='text', placeholder='Search...'),

    # Output component to display filtered DataFrame
    dash_table.DataTable(
        id='filtered-data',
        columns=[{'name': col, 'id': col} for col in address_filtered_df.columns],
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