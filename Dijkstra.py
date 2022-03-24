
#If graph is sparse we should use a binary Heap
class Item:
    def __init__(self, label, key):
        self.label, self.key = label, key

class PriorityQueueHeap():
    def __init__(self):
        self.A = []
        self.label2idx = {} #We implement a hash to accelerate searching for a vertex
    
    def min_heapify_up(self, c):
        if c == 0:
            return
        p = (c - 1) // 2
        if self.A[p].key > self.A[c].key:
            self.A[p].key, self.A[c].key = self.A[c].key, self.A[p].key 
            self.label2idx[self.A[c].label] = c
            self.min_heapify_up(p)

    def min_heapify_down(self, p):
        if p >= len(self.A):
            return
        l = 2 * p + 1
        r = 2 * p + 2
        if l >= len(self.A):
            l = p
        if r >= len(self.A):
            r = p
        c = l if self.A[r].key > self.A[l].key else r
        if self.A[p].key > self.A[c].key:
            self.A[c], self.A[p] = self.A[p], self.A[c]
            self.label2idx[self.A[c].label] = c
            self.label2idx[self.A[p].label] = p
            self.min_heapify_down(c)
        
    def insert(self, label, key):
        self.A.append(Item(label, key))
        idx = len(self.A) - 1
        self.label2idx[self.A[idx].label] = idx
        self.min_heapify_up(idx)
    

    def extract_min(self):
        self.A[0], self.A[-1] = self.A[-1], self.A[0]
        self.label2idx[self.A[0].label] = 0
        del self.label2idx[self.A[-1].label]
        min_label = self.A.pop().label
        self.min_heapify_down(0)
        return min_label

    
    def decrease_key(self, label, key): # decrease key of a given label
       if label in self.label2idx:
            idx = self.label2idx[label]
            if key < self.A[idx].key:
                self.A[idx].key = key
                self.min_heapify_up(idx)



#If graph is dense we can use normal array
class PriorityQueueArray():
    def __init__(self):
        self.A = {}
    
    def insert(self, label, key):
        self.A[label] = key
    
    def extract_min(self):
        min_label = None
        for label in self.A:
            if label is None or self.A[label] > self.A[min_label]:
                min_label = label
        del self.A[min_label]
        return min_label
    
    def decrease_key(self, label, key):
        if label in self.A and self.A[label] > key:
            self.A[label] = key


def try_to_relax(Adj, w,d,parent,u,v):
    if d[v] > d[u] + w(u,v):
        d[v] = d[u] + w(u,v)
        parent[v] = u


def dijkstra(Adj, w, s):
    distance = [float("inf") for node in Adj]
    parent = [None for node in Adj]
    distance[s], parent[s] = 0, s
    Q = PriorityQueueHeap() # Here we select wich type of DS we want for the PQ
    amountOfVertices = len(Adj)
    for _ in range(amountOfVertices):
        u = Q.extract_min()
        for v in Adj[u]:
            try_to_relax(Adj, w, distance, parent, u, v)
            Q.decrease_key(v, distance[v])
    return distance, parent 
   
            


