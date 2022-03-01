class BST_Node:
    def __init__(self, data):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data
        
    def subtree_first(self, A):
        if A.left == None:
            return A
        else:
            return self.subtree_first(A.left)
    
    def subtree_last(self, A):
        if A.right == None:
            return A
        else:
            return self.subtree_last(A.right)

    
    def recursive_iter(self, A):
        if A.left:
           yield from self.recursive_iter(A.left)
        yield A.data
        if A:
            yield from self.recursive_iter(A.right)
    

    def iter(self, A):
        stack = []
        curr = A
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                yield curr
                curr = curr.right
    
    def successor(self , A):
        if A.right:
            return self.subtree_first(A.right)
        else:
            while A.parent:
                if A.parent.left == A:
                    return A.parent.data
                else:
                    A = A.parent
                
    def predecessor(self, A):
        if A.left:
            return self.subtree_last(A.left)
        else:
            while A.parent:
                if A.parent.right == A:
                    return A.parent.data
                else:
                    A = A.parent
    
    def subtree_insert_before(self ,A , B):
        if A.left == None:
            A.left = B
            B.parent = A
        else:
            node = self.subtree_last(A.left)
            node.right = B
            B.parent = node
    
    def subtree_insert_after(self, A , B):
        if A.right == None:
            A.right = B
            B.parent = A
        else:
            node = self.subtree_first(A.right)
            node.left = B
            B.parent = node
    

    def subtree_delete(self, A):
        if A.left == None and A.right == None:
            if A.parent.left == A:
                A.parent.left = None
                A.parent = None
                return A
            if A.parent.right == A:
                A.parent.right = None
                A.parent = None
                return A
        else:
            if A.left:
                node = self.predecessor(A)
            else:
                node = self.successor(A)
            A.data, node.data = node.data, A.data
            return self.subtree_delete(node)
    
    def subtree_find(self, A, x):
        if A.data > x:
            if A.left:
                return self.subtree_find(A.left, x)
        elif A.data < x:
            if A.right:
                return self.subtree_find(A.right, x)
        else:
            return A
        return None


    def subtree_find_next(self, A, k):
        if A.data <= k:
            if A.right:
                return self.subtree_find_next(A.right,k)
            else:
                return None
        elif A.left:
            node = self.subtree_find_next(A.left, k)
            if node:
                return node
        return A


    def subtree_find_prev(self, A, k):
        if A.data >= k:
            if A.left:
                return self.subtree_find_prev(A.left, k)
            else:
                return None
        elif A.right:
            node = self.subtree_find_next(A.right, k)
            if node:
                return node
        return A

    
    def subtree_insert(self,A,B):
        if B.data < A.data:
            if A.left:
                return self.subtree_insert(A.left,B)
            else:
                return self.subtree_insert_before(A,B)
        elif B.data > A.data:
            if A.right:
                return self.subtree_insert(A.right,B)
            else:
                return self.subtree_insert_after(A,B)
    

class Binary_Search_Tree(BST_Node):
    def __init__(self):
        self.root = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        for i in self.iter(self.root):
            yield i.data

    def __str__(self):
        return "--".join([str(i) for i in self])

    
    def min(self):
        if self.root:
            return self.subtree_first(self.root).data
    def max(self):
        if self.root:
            return self.subtree_last(self.root).data
    
    def find(self, k):
        if self.root:
            node = self.subtree_find(self.root, k)
            if node:
                return "Found!"
            else:
                return "Not Found"
    
    def find_next(self, k):
        if self.root:
            node = self.subtree_find_next(self.root, k)
            return node.data
    def find_prev(self, k):
        if self.root:
            node = self.subtree_find_prev(self.root, k)
            return node.data
    
    def add(self, data):
        node = BST_Node(data)
        if not self.root:
            self.root = node
        else:
            self.subtree_insert(self.root, node)
            if node.parent == None:
                return False
        self.size += 1
        return True
    
    def delete(self, k):
        if self.root:
            node = self.subtree_find(self.root, k)
            if node:
                ext = self.subtree_delete(node)
                self.size -= 1
                return ext.data
    
    def sortedArraytoBST(self, A):
        sorted_array = A.sort()

        def build(l, r):
            if l > r:
                return None
            
            mid = (l + r) // 2
            node = BST_Node(sorted_array[mid])
            node.left = build(l, mid - 1)
            node.right = build(mid + 1 , r)
            return node
        self.root = build(0, len(A) - 1)
       

#testing
t = Binary_Search_Tree()

t.add(8)
t.add(3)
t.add(10)
t.add(25)
t.add(1)

print(t.max())




    
    
    
