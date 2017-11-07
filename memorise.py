from collections import Counter
from sys import stdin,stdout

n= int(stdin.readline())

arr = [int(x) for x in stdin.readline().split()]
C = Counter(arr)

q = int(stdin.readline())

for _ in range(q):
    
    a = int(stdin.readline())
    
    if(C[a]>0):
        stdout.write(str(C[a])+"\n")

    else:
        stdout.write("NOT PRESENT\n")
