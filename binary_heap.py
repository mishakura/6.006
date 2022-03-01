class binary_heap:
    def __init__(self, size):
        self.storage = [0 for i in range(7)]
        self.len = 0
        self.size = size

    def get_parent_index(self,index):
        parent = (index - 1) // 2
        return parent    

    def get_l_child_index(self,index):
        l_child = (2*index) + 1
        return l_child

    def get_r_child_index(self,index):
        r_child = (2*index) + 2
        return r_child

    def has_parent(self,index):
        if self.get_parent_index(index) >= 0:
            return True
        else:
            return False

    def has_l_child(self,index):
        if self.get_l_child_index(index) < self.size:
            return True
        else:
            return False

    def has_r_child(self,index):
        if self.get_r_child_index(index) < self.size:
            return True
        else:
            return False

    def get_parent_item(self,index):
        return self.storage[self.get_parent_index(index)]

    def get_l_child_item(self,index):
        return self.storage[self.get_l_child_index(index)]

    def get_r_child_item(self,index):
        return self.storage[self.get_r_child_index(index)]

    def is_full(self):
        if self.len == self.size:
            return True
        else:
            return False

    def swap(self, index1, index2):
        tmp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = tmp  

    def insert(self, data):
        if self.is_full():
            raise("Heap is full")
        else:
            self.storage[self.len] = data
            self.len += 1
            self.heapify_up()

    def heapify_up(self):
        index = self.len - 1
        test1 = self.get_parent_item(index)
        test2 = self.storage[index]
        while self.has_parent(index) == True and self.get_parent_item(index) < self.storage[index]:
            self.swap(self.get_parent_index(index),index)
            index = self.get_parent_index(index)

    def remove_first(self):
        if self.len == 0:
            raise("Empty heap")
        data = self.storage[0]
        self.storage[0] = self.storage[self.len - 1]
        self.storage[self.len - 1] = data
        self.len -= 1
        self.heapify_down()
        return data

    def heapify_down(self):
        index = 0
        while self.has_l_child(index):
            smallerChildIndex = self.get_l_child_index(index)
            if self.has_r_child(index) and self.get_r_child_item(index) > self.storage[smallerChildIndex]:
                smallerChildIndex = self.get_r_child_index(index)
            if self.storage[index] > self.storage[smallerChildIndex]:
                break
            else:
                self.swap(index, smallerChildIndex)
                index = smallerChildIndex  
    

          


        








            





bh = binary_heap(7)
bh.insert(5)
bh.insert(7)
bh.insert(10)
bh.insert(11)
bh.insert(15)
bh.insert(6)
bh.insert(19)

bh.remove_first()
print(bh.storage)












