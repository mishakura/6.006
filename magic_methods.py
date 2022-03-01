class Operators:
    op = []
    def __init__(self, x, y):
        self.x = x
        self.y = y

        Operators.op.append(self)

    
    def __repr__(self):
        return f'Operators({self.x}, {self.y})'

    def __str__(self):
        return f'{self.x}, {self.y}'
    
    def __add__(self, other):
        if type(other) == int:
            return Operators(self.x + other, self.y + other)
        else:
            return Operators(self.x + other.x, self.y + other.y)
    
    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        if type(other) == int:
            return Operators(self.x + other, self.y + other)
        else:
            return Operators(self.x + other.x, self.y + other.y)
    

    def __sub__(self, other):
        if type(other) == int:
            return Operators(self.x - other, self.y - other)
        else:
            return Operators(self.x - other.x , self.y - other.y)

    def __mul__(self, other):
        if type(other) == int:
            return Operators(self.x * other, self.y * other)
        else:
            return Operators(self.x * other.x, self.y * other.y)
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, other):
        if type(other) == int:
            return Operators(self.x / other, self.y / other)
        else:
            return Operators(self.x / other.x, self.y / other.y)

    def __eq__(self, other):
        if self.x == other.x:
            return True
        else:
            return False
    
    def __ne__(self, other):
        if self.x != other.x:
            return True
        else:
            False
    
    def __lt__(self, other):
        if self.x < other.x:
            return True
        else:
            return False
    
    def __gt__(self, other):
        if self.x > other.x:
            return True
        else:
            return False

    def __le__(self, other):
        if self.x <= other.x:
            return True
        else:
            return False
    
    def __ge__(self, other):
        if self.x >= other.x:
            return True
        else:
            return False
    
    def __int__(self):
        return int(self.y)

    def __call__(self, k):
        return (self.x * self.y) * k


class ObjMulItems:
    def __init__(self, awa , dictionary):
        self.dictionary = dictionary
        self.awa = awa

    def __len__(self):
        return len(self.dictionary)  
    
    def __getitem__(self, key):
        return self.dictionary[key]
    
    def __setitem__(self, key, val):
        self.dictionary[key] = val
    
    def __delitem__(self , key):
        print(self.dictionary[key])
        del self.dictionary[key]


class Mammal():
     
    def __init__(self, name):
        print(name, "Is a mammal")
         
class canFly(Mammal):
     
    def __init__(self, canFly_name):
        print(canFly_name, "cannot fly")
         
        # Calling Parent class
        # Constructor
        super().__init__(canFly_name)
             
class canSwim(Mammal):
     
    def __init__(self, canSwim_name):
         
        print(canSwim_name, "cannot swim")
             
        super().__init__(canSwim_name)
         
class Animal(canFly, canSwim):
     
    def __init__(self, name):
         
        # Calling the constructor
        # of both thr parent
        # class in the order of
        # their inheritance
        super().__init__(name)
 
 
# Driver Code

    

# student1 = (105, "Mikael", "France")
# student2 = (106, "Corgi", "Idiot")

# students = {hash("Mikael"): student1, hash("Corgi"): student2}
# awa = 4
# obj = ObjMulItems(awa, students)
# print(len(obj))
# obj[hash("Armando")] = (107, "Theo", "Canadian for sure")
# print(len(obj))
# print(obj[hash("Armando")])

# del obj[hash("Corgi")]
# print(len(obj))




# a = Operators(10, 20)
# b = Operators(30,50)
# c = Operators(150,200)
# d = Operators(10,20)












