# Create random data with numpy
import numpy as np
import plotly.graph_objs as go
import plotly.plotly as py

N = 1000
random_x = np.random.randn(N)
random_y = np.random.randn(N)

# Create a trace
trace = go.Scatter(
    x=random_x,
    y=random_y,
    mode='markers'
)

data = [trace]

# Plot and embed in ipython notebook!
py.iplot(data, filename='basic-scatter')

# or plot with:
# py.plot(data, filename='basic-scatter.html')
