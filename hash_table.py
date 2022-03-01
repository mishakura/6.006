
class HashTable():
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]
    def hash(self, key):
        k = 0
        m = len(key) + 100
        p = 9419
        
        for i in key:
            k += ord(i)
        return ((k%p) % m)

    def __setitem__(self, key, value):
        h = self.hash(key)
        found = False
        for i , element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][i] = (key,value)
                found = True
                break
        if found == False:
            self.arr[h].append((key, value))

    def __getitem__(self,key):
        h = self.hash(key)
        if len(self.arr[h]) == 1:
            return self.arr[h][0][1]     
        else:
            for i in range(len(self.arr[h])):
                if self.arr[h][i][0] == key:
                    return self.arr[h][i][1]
                    
    def __delitem__(self, key):
        h = self.hash(key)
        for i , element in enumerate(self.arr[h]):
            if self.arr[h][i][0] == key:
                del self.arr[h][i]

     

                         










