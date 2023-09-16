# import dash
# from dash import dcc, html, Input, Output
# import pandas as pd
# import plotly.express as px
# import dash_table
# from dash_extensions import Download
#
# # Sample DataFrame
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
#     'Age': [25, 30, 35, 28, 22],
#     'Gender': ['Female', 'Male', 'Male', 'Male', 'Female'],
#     'Salary': [50000, 60000, 75000, 55000, 48000],
#     'Revenue': [2500, 3000, 3500, 2800, 2200]
# }
#
# # Create the DataFrame
# df = pd.DataFrame(data)
#
# # Initialize the Dash app
# app = dash.Dash(__name__)
#
# # Define the app layout
# app.layout = html.Div([
#     dcc.Input(id='filter-input', type='text', placeholder='Search...'),
#     html.Br(),
#     dash_table.DataTable(
#         id='filtered-data',
#         columns=[
#             {'name': col, 'id': col} for col in df.columns
#         ],
#         style_table={'width': '100%'},
#         style_header={'textAlign': 'left'},
#         page_size=10,  # Number of rows per page
#         sort_action='native',  # Enable native sorting
#         sort_mode='multi',  # Enable multi-column sorting
#     ),
#     html.Br(),
#     html.Button('Download as Excel', id='btn-excel', n_clicks=0),
#     html.Button('Download as PDF', id='btn-pdf', n_clicks=0),
#     Download(id="download"),
# ])
#
# # Callback to update the filtered table and enable downloads
# @app.callback(
#     [Output('filtered-data', 'data'),
#      Output('download', 'data')],
#     [Input('filter-input', 'value'),
#      Input('btn-excel', 'n_clicks'),
#      Input('btn-pdf', 'n_clicks')]
# )
# def update_table_and_downloads(search_term, excel_clicks, pdf_clicks):
#     if search_term is None:
#         search_term = ""  # Default to an empty string if search_term is None
#
#     # Filter the DataFrame based on the search term
#     filtered_df = df[df.apply(lambda row: search_term.lower() in ' '.join(map(str, row)).lower(), axis=1)]
#
#     # Create a dictionary to hold data for download
#     download_data = {
#         'filtered_data.csv': filtered_df.to_csv(index=False, encoding='utf-8'),
#         'filtered_data.pdf': '<pdf_content_here>'
#     }
#
#     # Check which download button was clicked and trigger the corresponding download
#     ctx = dash.callback_context
#     if ctx.triggered:
#         prop_id = ctx.triggered[0]['prop_id']
#         if prop_id == 'btn-excel.n_clicks':
#             return filtered_df.to_dict('records'), download_data['filtered_data.csv']
#         elif prop_id == 'btn-pdf.n_clicks':
#             return filtered_df.to_dict('records'), download_data['filtered_data.pdf']
#
#     return filtered_df.to_dict('records'), None
#
# # Run the app
# if __name__ == '__main__':
#     app.run_server(debug=True)

import dash
from dash import dcc, html, Input, Output
from dash.exceptions import PreventUpdate
from dash import dash_table as dt
import pandas as pd
import io

# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}
df = pd.DataFrame(data)

app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    dcc.Download(id="download-excel-button"),
    dt.DataTable(
        id='data-table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
    ),
    html.Button("Download Excel", id="excel-button"),
])

# Callback to trigger Excel download
@app.callback(
    Output("download-excel-button", "data"),
    Input("excel-button", "n_clicks"),
)
def download_excel(n_clicks):
    if not n_clicks:
        raise PreventUpdate

    # Create a BytesIO buffer for the Excel file
    buffer = io.BytesIO()

    # Create a Pandas Excel writer using XlsxWriter as the engine
    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Sheet1', index=False)

    buffer.seek(0)

    return dict(
        content=buffer.getvalue(),
        filename="data.xlsx"
    )

if __name__ == '__main__':
    app.run_server(debug=True)
