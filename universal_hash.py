# (((a*k+b)mod p)mod m)
#a != 0 , a and b radomized and should be less than p - 1, p is a primestatic number > n.
import random

def uni_hash(key,n):
    ASCII_key = 0
    m = len(n) + 100
    p = 9419
    a = 2 #Could be any number > 0
    b = 3 #Could be any number >= 0

    if type(key) == str:
        for i in range(len(key)):
            ASCII_key += ord(key[i])
        return (((a*ASCII_key+b)% p)% m)    
    else:
        return (((a*key+b)% p)% m)

    


