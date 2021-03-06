def dfs(Adj, s, parent = None, order = None):
    if parent == None:
        parent = [None for vertice in Adj] 
        parent[s] = s
        order = []
    for vertice in Adj[s]:
        if parent[vertice] is None:
            parent[vertice] = s
            dfs(Adj, vertice, parent, order)
    order.append(s)
    return parent, order

def full_dfs(Adj):
    parent = [None for vertice in Adj]
    order = []
    for vertice in range(len(Adj)):
        if parent[vertice] is None:
            parent[vertice] = vertice
            dfs(Adj, vertice, parent, order)
    return parent,order

Adj = {0:[4],1:[], 2:[1], 3:[2],4:[5,3],5:[1,2]}        