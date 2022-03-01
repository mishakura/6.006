#queue using Linked list
class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next
        

class Queue():
    def __init__(self):
        self.head = None
        self.tail = None
        self.itr = None
    
    def Enqueue(self, data):
        node = Node(data, self.tail)
        if self.head == None:
            self.head = node
            self.itr = self.head
            self.tail = node
        else:
            self.itr.next = node
            self.tail = node
            self.itr = self.itr.next
            
    def Dequeue(self):
        value = self.head.data
        self.head = self.head.next

    def Front(self):
        return self.head.data

    def Rear(self):
        return self.tail.data          
        
    def list_values(self):
        list = []
        itr = self.head
        while itr:
            list.append(itr.data)
            itr = itr.next
        return list

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False            

        





q = Queue()
q.Enqueue(5)
q.Enqueue(6)
q.Enqueue(8)

print(q.is_empty())



