   #Adj = {0:  [4]
#       1 : [5,2]
#       2 : [5,1,3]
#       3 : [4,2]
#       4 : [0,3,5]
#       5 : [1,2]}

parent = {s: None} #[0: None, 4: 0, 3 : 4, 2:]
def DFS(Adj, s):
    for v in Adj[s]:
        if v not in parent:
            parent[v] = s
            DFS(Adj,v)


