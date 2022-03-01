def height(A):
    if A:
        return A.height
    else:
        return -1

class BST_Node():
    def __init__(self,data):
        self.left = None
        self.right = None
        self.parent = None
        self.data = data
        self.subtreeUpdateHeight()
    
    def subtreeUpdateHeight(self, A):
        A.height = 1 + max(height(A.left), height(A.right))
    
    def skew(self, A):
        return height(A.right) - height(A.left)
    
    def subtreeIter(self, A):
        stack = []
        curr = A
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = A.left
            elif stack:
                curr = stack.pop()
                yield curr
                curr = curr.right
    
    def subtreeFirst(self, A):
        if A.left == None:
            return A
        else:
            return self.subtreeFirst(A.left)
    
    def subtreeLast(self, A):
        if A.right == None:
            return A
        else:
            return self.subtreeLast(A.right)

    def predecessor(self, A):
        if A.left:
            return self.subtreeLast(A.left)
        else:
            while A.parent:
                if A.parent.right == A:
                    return A.parent
                else:
                    A = A.parent
    
    def successor(self, A):
        if A.right:
            return self.subtreeFirst(A.right)
        else:
            while A.parent:
                if A.parent.left == A:
                    return A.parent
                else:
                    A = A.parent
    
    def subtreeInsertBefore(self, A, B):
        if A.left == None:
            A.left = B
            B.parent = A
        else:
            node = self.subtreeLast(A.left)
            node.right = B
            B.parent = node
        A.mantain()

    
    def subtreeInsertAfter(self, A, B):
        if A.right == None:
            A.right = B
            B.parent = A
        else:
            node = self.subtreeFirst(A.right)
            node.left = B
            B.parent = node
        A.maintain()

    def subtreeDelete(self, A):
        if A.left == None and A.right == None:
            if A.parent.left == A:
                A.parent.left = None
                A.parent = None
            elif A.parent.right == A:
                A.parent.right = None
                A.parent = None
            A.maintain()
        else:
            if A.left:
                node = self.predecessor(A)
            elif A.right:
                node = self.successor(A)
            A.data, node.data = node.data, A.data
            return self.subtreeDelete(node)
    
    def subtreeRotateRight(self, D):
        assert D.left
        B, E = D.left, D.right
        A, C = B.left, B.right
        D, B = B, D
        B.item, D.item = D.item, B.item
        B.left, B.right = A, D
        D.left, D.right = C, E
        if A:
            A.parent = B
        if E:
            E.parent = D
        self.subtreeUpdateHeight(D)
        self.subtreeUpdateHeight(B)
    
    def subtreeRotateLeft(self, B):
        A, D = B.left, B.right
        C, E = D.left, D.right
        D, B = B, D
        D.item, B.item = B.item, D.item
        D.left, D.right = B, E
        B.left, B.right = A, C
        if E:
            E.parent = D
        if A:
            A.parent = B
        self.subtreeUpdateHeight(B)
        self.subtreeUpdateHeight(D)

    def rebalance(self, A):
        if self.skew(A) == 2:
            if self.skew(A.right) < 0:
                self.subtreeRotateRight(A)        
            self.subtreeRotateLeft(A)
        elif self.skew(A) == -2:
            if self.skew(A.left) > 0:
                self.subtreeRotateLeft(A)
            self.subtreeRotateRight(A)
    
    def maintain(self, A):
        self.rebalance(A)
        self.subtreeUpdateHeight(A)
        if A.parent:
            self.maintain(A.parent)

    



        



    
        
        


    
    





            
             




            
        





    


    


    

     
    




    








