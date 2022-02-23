
import math 
import random
msg = int(input("Enter the message to encrypt and decrypt"))
p = int(input("Enter Large prime nuber P"))
q = int(input("Enter Large prime number Q"))
#p = int(input())
#calculation of e as coprime !!!!!
phi= (p-1)*(q-1)
e =  random.randint(1,phi)
n= p*q

def encryption(me):
    en=math.pow(me,e)
    c = en % n
    print("After encryption",c)
    return c
        
print("Original Message is: ", msg)
c = encryption(msg)