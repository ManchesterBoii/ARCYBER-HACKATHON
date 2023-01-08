import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

URIPathVis = dash.Dash(__name__, 
                external_stylesheets=external_stylesheets,
                requests_pathname_prefix='/URIPathVis/'
                
                )

filepath = "[OQ] Reverse Proxy Command Injection (Non-Army.csv"


def timestamps(time_lst):
    return [pd.Timestamp(int(time_in_ms), unit="ms") for time_in_ms in time_lst]

df = pd.read_csv(filepath, index_col=0, parse_dates=True, date_parser=timestamps, header = 0, usecols= ["Timestamp", "BYTES_INPUT", "BYTES_OUTPUT","TYPE_ATTACK","URI_PATH"] )

fig = px.scatter(df, x="BYTES_INPUT", y="BYTES_OUTPUT", color="TYPE_ATTACK", hover_name="URI_PATH", log_x=True, size_max=60)



URIPathVis.layout = html.Div([
    html.H1("Possible webShell Visual"),
    dcc.Graph(
        id='Possible-webShell-Visual',
        figure=fig
    ),
    html.A('Return Home', href = 'http://localhost:8050/')
    
])


