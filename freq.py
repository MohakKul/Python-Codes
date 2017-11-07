q= input()
A= list(map(int,input().split()))
B= set(A[:])
C= []
D= list(B)
D.sort()
D= [item for item in D if item>=0]
E=D[:]
if(len(D)==1):
   print(E[0])
else:   
    for i in (1,len(A)):
        C.append(A.count(D.pop(0)))   
    print(E[C.index(max(C))])
