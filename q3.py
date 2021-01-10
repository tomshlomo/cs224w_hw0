import snap
import numpy as np
import plotly.express as px
import plotly.graph_objs as go

G = snap.LoadEdgeList(snap.TNGraph, "stackoverflow-Java.txt", 0, 1)
print(f'wcc: {G.GetWccs()}')
G2 = G.GetMxWcc()
print(f'Nodes: {G2.GetNodes()}, Edges: {G2.GetEdges()}')

PRankH = G.GetPageRank()
r = np.zeros(G.GetNodes())
id = np.zeros(G.GetNodes())
for i, item in enumerate(PRankH):
    r[i] = PRankH[item]
    id[i] = item
i = r.argsort()
for j in [-1, -2, -3]:
    print(id[i[j]], r[i[j]])


NIdHubH, NIdAuthH = G.GetHits()
for i, item in enumerate(NIdAuthH):
    r[i] = NIdAuthH[item]
    id[i] = item
i = r.argsort()
for j in [-1, -2, -3]:
    print(id[i[j]], r[i[j]])
pass
