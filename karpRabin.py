#ClRS Algorithm
# magic = (base ** len(n)) % prime number
#Add char to multidigt number = (n * base) + new
#Remove char to multidigt number = n - old * base **((len n) - 1)
# = (n - old * base **((len n) - 1)) * base + new
# = ((n * base - old * magic ) + new) % primeNumber
# In order to recude big number we can distribute mod to the bigger numbers and reduce runtime
# ((n % primeNumber * base - old * magic) + new) % primeNumber

def rabinKarp(pattern, text, primeNumber):
    base = 256
    pl = len(pattern)
    tl = len(text)
    i = 0
    j = 0
    textHash = 0
    patternHash = 0
    magic = 1

    for i in range(pl - 1):
        magic = (magic * base) % primeNumber
    
    for i in range(pl):
        patternHash = (patternHash * base) + ord(pattern[i]) % primeNumber
        textHash = (textHash * base) + ord(text[i]) % primeNumber
    
    for i in range(tl - pl + 1):
        if patternHash == textHash:
            for j in range(pl):
                if text[i + j] != pattern[i]:
                    break
                else:
                    j += 1
        if j == pl:
            print(f"Pattern found at index {i}")
        
        if i < tl - pl:
            hashText = ((hashText  * base - ord(text[i]) * magic) + ord(text[i + pl])) % primeNumber
            if hashText < 0:
                hashText = hashText + patternHash





        
        









        
        



        

                
        
            
            




    
    





