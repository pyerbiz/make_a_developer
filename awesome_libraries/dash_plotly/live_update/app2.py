import dash
import dash_html_components as html
import dash_core_components as dcc
import numpy as np
import pandas as pd


from dash.dependencies import Input, Output


datafile=r"C:\Users\saral\OneDrive\Desktop\projects\data\timedata.csv"
data=pd.read_csv(datafile)

resolution = 2000000
x, y = data.index, data["HoleDepth (ft)"]

#DATE	AD_DiffPressure_Setpoint (psi)	AD_ROP_Setpoint (ft/hr)	AD_WOB_Setpoint (klb)	BitDepth (ft)	BlockPostion (ft)	HoleDepth (ft)	HookloadMax (klb)	MudFlowInAvg (gpm)	RigState	ROPAvg (ft/hr)	RPMA (rpm)


# Example app.
figure = dict(data=[{'x': [], 'y': []}]) #layout=dict(xaxis=dict(range=[0, 1000000]), yaxis=dict(range=[0, 25000])))

app = dash.Dash(__name__, update_title=None)  # remove "Updating..." from title
app.layout = html.Div([dcc.Graph(id='graph', figure=figure), dcc.Interval(id="interval")])


@app.callback(Output('graph', 'extendData'), [Input('interval', 'n_intervals')])
def update_data(n_intervals):
    index = n_intervals % resolution
    # tuple is (dict of new data, target trace index, number of points to keep)
    return dict(x=[[x[index]]], y=[[y[index]]]), [0]


if __name__ == '__main__':
    app.run_server()