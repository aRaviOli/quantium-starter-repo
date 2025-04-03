from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px


DATA_FILE = '../output/pink_morsel_sales.csv'

app = Dash(__name__)

df = pd.read_csv(DATA_FILE)
df = df.sort_values(by='date', ascending=True)

line_chart = px.line(df, x='date', y='sales', color='region', title='Pink Morsel')

# app layout
app.layout = html.Div(children=[
    html.H1(children='pink morsel visualiser'),

    html.Div(children='''
        Pink Morsel Sales
    '''),

    dcc.Graph(
        id='visualiser',
        figure=line_chart
    )
])


if __name__ == "__main__":
    app.run(debug=True, port=8000)
