from heapq import merge


class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insert_start(self, data):
        node = Node(data, self.head)
        self.head = node
        

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next
    def __str__(self):
        return "-->".join([('(%s)' % x) for x in self])      
           


    def insert_end(self, data):
        itr = self.head
        if itr == None:
            node = Node(data, None)
            self.head = node
            self.size += 1
            
        while itr != None:
            if itr.next == None:
                node = Node(data, None)
                itr.next = node
                self.size += 1
                break
            itr = itr.next

    def insert_multiple_values(self, list):
        for i in list:
            self.insert_end(i)
            

    def length(self):
        itr = self.head
        len = 0
        while itr != None:
            len += 1
            itr = itr.next
        return len
   
    
    def remove_at(self, index):
        if index < 0 or index > self.length():
            raise Exception("Invalid index")
        elif index == 0:   
            self.head = self.head.next
            self.size -= 1
        else:
            counter = 0
            itr = self.head
            while itr:
                if index - 1 == counter:
                    itr.next = itr.next.next
                    self.size -= 1
                    break
                
                itr = itr.next  
                counter += 1 

    def insert_at(self, index, data):
        if index > self.length() or index < 0:
            raise Exception("Invalid index or empty linked list")

        if index == 0:
            self.insert_start(data)
            self.size += 1
        else:
            counter = 0
            itr = self.head
            while itr != None:
                if counter  == index - 1:
                    node = Node(data, itr.next)
                    itr.next = node
                    self.size += 1
                    break
                counter += 1
                itr = itr.next 


    def reverse(self):
        head = self.head
        next_node = self.head.next
        current = self.head
        prev = None
        while True:
            current.next = prev
            prev = current       
            current = next_node
            if current == None:
                self.head = prev
                break
            next_node = next_node.next 

    def recursive(self, node):
        if node == None:
            return
        if node.next == None:
            self.head = node
            return    
        self.recursive(node.next)
        curr = node
        curr.next.next = curr
        curr.next = None

    def reverse_half(self):
        n = self.length() // 2
        a = self.head
        for i in range(n-1):
            a = a.next
        b = a.next    
        current = a.next
        prev = None
        xn = a.next.next
        while current != None:
            current.next = prev
            prev = current
            current = xn
            if current == None:
                break
            xn = xn.next
        a.next = prev
        b = None
            


def mergeTwo(list1, list2):
        if list1 and list2 == None:
            return list1
        elif list1 == None and list2:
            return list2
        elif list1 == None and list2 == None:
            return None
        prev = None
        newHead = None
        if list1.val < list2.val:
            newHead = list1
            prev = list1
            list1 = list1.next
        else:
            newHead = list2
            prev = list2
            list2 = list2.next
    
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                prev = list1
                list1 = list1.next
            else:
                prev.next = list2
                prev = list2
                list2 = list2.next
    
        if list1:
            prev.next = list1
        else:
            prev.next = list2
        return newHead








list1 = [1,2,10]
list2 = [3,4,150]

linked_list1 = LinkedList()
linked_list1.insert_multiple_values(list1)

linked_list2 = LinkedList()
linked_list2.insert_multiple_values(list2)

ll = LinkedList()
ll.head = mergeTwo(linked_list1.head, linked_list2.head)
for i in ll:
    print(i)







               
    

