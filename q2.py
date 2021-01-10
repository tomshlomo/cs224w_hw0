import snap
import numpy as np
import plotly.express as px
import plotly.graph_objs as go

G = snap.LoadEdgeList(snap.TNGraph, "wiki-Vote.txt", 0, 1)
out_deg = G.GetOutDegCnt()
x = np.array([p.GetVal1() for p in out_deg])
y = np.array([p.GetVal2() for p in out_deg])
I = (x > 0) & (y > 0)
x = x[I]
y = y[I]

fig = px.scatter(x=np.log10(x), y=np.log10(y))
fig.show()

p = np.polyfit(np.log10(x), np.log10(y), deg=1)
print(p)

x_plot = np.log10(x[[0, -1]])
y_plot = np.polyval(p, x_plot)
fig.add_trace(go.Line(x=x_plot, y=y_plot))
fig.show()
pass
