import snap

G = snap.LoadEdgeList(snap.TNGraph, "wiki-Vote.txt", 0, 1)

# 1
print(f'Num nodes: {G.GetNodes()}')

# 2
self_loops = [edge for edge in G.Edges() if edge.GetSrcNId() == edge.GetDstNId()]
print(f'Self loops: {len(self_loops)}')

# 3
directed_edges = {(edge.GetSrcNId(), edge.GetDstNId()) for edge in G.Edges() if not edge.GetSrcNId() == edge.GetDstNId()}
print(f'directed_edges: {len(directed_edges)}')

# 4
undirected_edges = {frozenset([edge.GetSrcNId(), edge.GetDstNId()]) for edge in G.Edges()
                   if not edge.GetSrcNId() == edge.GetDstNId()}
print(f'undirected_edges: {len(undirected_edges)}')

# 5
reciprocated_edges = {frozenset([*edge]) for edge in directed_edges if edge[::-1] in directed_edges}
print(f'reciprocated_edges: {len(reciprocated_edges)}')

# 6
out_deg = G.GetOutDegCnt()
print("out degree %d: count %d" % (out_deg[0].GetVal1(), out_deg[0].GetVal2()))

# 7
in_deg = G.GetInDegCnt()
print("in degree %d: count %d" % (in_deg[0].GetVal1(), in_deg[0].GetVal2()))

# 8
n = 0
for p in out_deg:
    if p.GetVal1() > 10:
        n += p.GetVal2()
print(f'n = {n}')

# 9
n = 0
for p in in_deg:
    if p.GetVal1() < 10:
        n += p.GetVal2()
print(f'n = {n}')

pass