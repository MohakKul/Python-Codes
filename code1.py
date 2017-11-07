a= list(map(int,input().split()))
b= a[0]
a.pop(0)
a.sort()
for i in range(0,b):
    print(a[i],end=' ')
