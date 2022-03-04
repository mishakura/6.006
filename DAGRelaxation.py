#Restrictions SSSP Algorithm
#Graph Weights Name Running Time O(·)
#General Unweighted - BFS - |V | + |E|
#Any Dag - DAG Relaxation - |V | + |E|
#General Any - Bellman-Ford - |V | · |E|
#General Non-negative- Dijkstra  - |V | log |V | + |E 

from DFS import dfs

def try_to_relax(Adj, w,d,parent,u,v):
    if d[v] > d[u] + w(u,v):
        d[v] = d[u] + w(u,v)
        parent[v] = u

def DAG_relaxation(Adj,w,s):
    _, order = dfs(Adj,s)
    order.reverse()
    d = [float("inf") for vertice in Adj]
    parent = [None for vertice in Adj]
    d[s] , parent[s] = 0,s
    for u in order:
        for v in Adj[u]:
            try_to_relax(Adj, w, d,parent,u,v)
    return d,parent