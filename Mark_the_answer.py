a,b= map(int,input().split())
c= list(map(int,input().split()))
c1=0
c2=0
for i in c:
    if (i<=b):
        c1+=1
    else:
        c2+=1
        if (c2>1):
            break
print (c1)        
