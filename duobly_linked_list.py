class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None
        self.tail_itr = None
        self.head_itr = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        ###########################
        # Part (a): Implement me! #
        ###########################
        node = Doubly_Linked_List_Node(x)
        
        if self.head == None:
            node.next = None
            node.prev = None
            self.head = node
            self.tail = node
            self.tail_itr = self.tail
            self.head_itr = self.head
        else:
            self.head = node
            node.prev = None
            node.next = self.tail_itr
            self.tail_itr.prev = node
            self.tail_itr = node


    def insert_last(self, x):
        ###########################
        # Part (a): Implement me! #
        ###########################
        node = Doubly_Linked_List_Node(x)

        if self.head == None:
            node.prev = None
            node.next = None
            self.head = node
            self.tail = node
            self.head_itr = self.head
            self.tail_itr = self.tail
        else:
            self.tail = node
            node.next = None
            node.prev = self.head_itr
            self.head_itr.next = node
            self.head_itr = node



    def delete_first(self):
        
        ###########################
        # Part (a): Implement me! #
        ###########################
        x = self.head.item
        self.head = self.head.next
        self.head.prev = None
        
        if self.head == None or self.head.item == None:
            raise Exception("Doubly Linked list is empty")
        
        
        return x

    def delete_last(self):
        
        ###########################
        # Part (a): Implement me! #
        ###########################
        x = self.tail.item
        self.tail = self.tail.prev
        self.tail.next = None
        if self.tail == None or self.tail.item == None:
            raise Exception("Doubly Linked list is empty")
        
        
        return x

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        ###########################
        # Part (b): Implement me! # 
        ###########################
        L2.head = x1
        L2.tail = x2
        if x1.prev:
            x1.prev.next = x2.next
        if x2.next:
            x2.next.prev = x1.prev
        L2.head.prev = None
        L2.tail.next = None
        return L2


       """ I missunderstood the problem and i did it with index lmao!
       counter = 0
        node = self.head
        fnode = None
        lnode = None
        while True:
            if x1 == 0:
                if counter == x1:
                    L2.head = node
                elif counter == x2:
                    L2.tail = node
                elif counter == x2+1:
                    node.prev = None
                    self.head = node
                    L2.tail.next = None
                    break

                counter += 1
                node = node.next        

            if x1 != 0:
                if counter == x1 -1:
                    fnode = node
                elif counter == x1:
                   L2.head = node
                
                elif counter == x2:
                   L2.tail = node
                   if node.next == None:
                       
                       L2.head.prev = None
                       L2.tail.next = None
                       
                       break
                
                elif counter == x2+1:
                   lnode = node
                   fnode.next = lnode
                   lnode.prev = fnode 
                   L2.head.prev = None
                   L2.tail.next = None
                   break
                 
                counter += 1
                node = node.next
            
            
        return L2  """





    def splice(self, x, L2):
        ###########################
        # Part (c): Implement me! # 
        ###########################
        if x.next:
            save_node = x.next
            x.next = L2.head
            L2.head.prev = x
            L2.tail.next = save_node
            save_node.prev = L2.tail.next
            
        else:
            x.next = L2.head
            L2.head.prev = x
            self.tail = zL2.tail
            
        L2.tail = None
        L2.head = None
        
        return















