### Plotting from a given list of integers
Create a scatter plot via updating list. Random values are generated into list for this example.
```python3
import dash, random
from dash import Dash, dcc, html, Input, Output, callback, Patch
import plotly.express as px

gui = Dash(__name__)
gui.layout = html.Div( # structures web app
    html.Div([
        html.H4('Frequency counter'),
        dcc.Graph(id='live-update-graph',style={'overflow-x': 'scroll'}),
        dcc.Interval(id='interval-component', interval=50),
    ])
)
x = []
y = []
count = 0

@callback(Output('live-update-graph', 'figure'),
 Input('interval-component', 'n_intervals'))
def live_status(n): # generate data and plot
    global count
    count += 1
    x.append(count)
    y.append(random.randint(1,5))     
    fig = px.scatter(x=x, y=y,)  
    fig.update_layout(xaxis_range=[0,count+100],   width=count+10000)
    return fig

if __name__ == '__main__': # run web app
    gui.run(debug=True,port=5000) 
```
### Plotting a noisy sine wave
Create a noisy sine wave using a scatter plot. Hz count can be adjusted via slider.
```python3
import dash, random
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import numpy as np

gui = Dash(__name__)
gui.layout = html.Div( # structures web app
    html.Div([
        html.H4('Frequency counter'),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(id='interval-component', interval=50),
        dcc.Slider(1,5,1, value=10,id='my-slider'),
        html.Div(id='slider-output-container')
    ])
)

@callback(Output('live-update-graph', 'figure'),
 Input('interval-component', 'n_intervals'),
 Input('my-slider', 'value'))
def live_status(n, slidervalue): # generate data and plot
    rng = np.random.default_rng()
    noise = rng.standard_normal(1024) #1024 points of noise
    x = np.linspace(0, 4, 1024)
    cycle = 2*3.14*x 
    Hz = cycle * slidervalue
    y = np.sin(Hz) + 0.1*noise
    fig = px.scatter(x=x, y=y,)
    fig.update_layout(xaxis_range=[0,4], yaxis_range=[-1.5,1.5])
    return fig

if __name__ == '__main__': # run web app
    gui.run(debug=True,port=5000)    
```
