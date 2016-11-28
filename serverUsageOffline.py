# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

#import plotly.plotly as py
import plotly.graph_objs as go


from plotly import __version__
#from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.offline import plot


trace1 = go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[40, 80, 80, 80, 70, 90, 50, 20, 10],
    name='HPG6-01'
)
trace2 = go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[10, 20, 30, 40, 70, 60, 50, 20, 10],
    name='HPG6-02 '
)
trace3 = go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[100, 80, 80, 80, 70, 40, 50, 20, 10],
    name='HPG6-03'
)
trace4 = go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[100, 70, 80, 80, 70, 60, 50, 20, 10],
    name='HPG6-04'
)
data = [trace1, trace2, trace3, trace4]
layout = go.Layout(
    title='Server Utilization VS Time',
    xaxis=dict(
        title='Time (Hours)',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Percentage Utilization',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)
fig = go.Figure(data=data, layout=layout)
plot_url = plot(fig, filename='first_example.html')
