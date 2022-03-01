#Dinamic array stack
class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()
        

    def peek(self):
        return self.stack[-1]

    def length(self):
        return len(self.stack)
        

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

deque = Stack()
deque.push(3)  
deque.push(5) 
deque.push(6)
print(deque.is_empty())
print(deque.pop())
print(deque.stack)     






                    