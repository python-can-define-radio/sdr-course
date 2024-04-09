# from pcdr.simple import OsmosdrWBFMTransmitter

# transmitter = OsmosdrWBFMTransmitter("hackrf=0", 104.3e6, plotly_gui="time_mod")
# transmitter.set_center_freq(104.5e6)
# transmitter.set_if_gain(23)

import numpy as np
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px


from pcdr.simple import AudioPlayer

vecsize = 16384
player = AudioPlayer(wavfile="drum_cowbell.wav",
                    audio_sample_rate=22050,
                    repeat=True)
player.connect_probe(location="audio_sink", vecsize=vecsize)


app = Dash(__name__)
app.layout = html.Div([
    dcc.Graph(id='live-update-graph'),
    dcc.Interval(
        id='interval-component',
        interval=2000, # in milliseconds
        n_intervals=0
    )
])


@callback(Output('live-update-graph', 'figure'),
          Input('interval-component', 'n_intervals'))
def update_graph_live(n):
    if n == 0:
        print("start")
        player.start()
    else:
        print(n)
    meas = player.read_probe()
    return px.scatter(y=meas)


if __name__ == '__main__':
    app.run(debug=True)
