q=input()
dc=list(map(int,input().split()))
for i in ls:
    if i in dc:
        dc[i]+=1
    else:
        dc[i]=1
k=max(dc.values())
ls=[]
for i in dc:
    if dc[i]==k:
        ls.append(i)
print(min(ls))
