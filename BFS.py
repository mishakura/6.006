#mit 6006 2020 bfs algorithm
def bfs(Adj, s):   #adjacency list(hash map), s: starting vertex
    #Adj = {0:  [4]
#       1 : [5,2]
#       2 : [5,1,3]
#       3 : [4,2]
#       4 : [0,5,3]
#       5 : [1,2]}
    parent = [None for vertex in Adj] #[4,5,5,4,0,4]
    #parent[s] = s #(Vertex 1)
    level = [[s]] #initialize levels - level 0 -vertex 0 
    #[[0], [4], [0,5,3], [1,2]]       
    while 0 < len(level[-1]):
        level.append([]) #create a new level
        for u in level[-2]: #
            for v in Adj[u]: # 
                if parent[v] is None:
                    parent[v] = u
                    level[-1].append(v)
    return parent
                                 









     






    
    



