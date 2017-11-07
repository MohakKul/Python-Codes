a= int(input())
while(a):
    b= int(input())
    c= list(input())
    d=[]
    e=[]
    f=[]
    g=[]
    for i in c:
        d.append((ord(i)))
    for k in d:
        for i in range(k,0,-1):
            for j in range(2,i):
                if(i%j)==0:
                    break
            else:
                e.append(i)
                break
    for k in d:
        for i in range(k,128):
            for j in range(2,i):
                if(i%j)==0:
                    break
            else:
                f.append(i)
                break
    for i in range(0,len(c)):
        x=d[i]-e[i]
        y=f[i]-d[i]
        if((x<=y)):
            if((e[i]>=65 and e[i]<=90)or(e[i]>=97 and e[i]<=122)):
               g.append(e[i])
            elif(e[i]<65):
                g.append(67)
            elif(e[i]>122):
                g.append(113)
            else:
               g.append(f[i])
        else:
            if((f[i]>=65 and f[i]<=90)or(f[i]>=97 and f[i]<=122)):
               g.append(f[i])
            elif(f[i]<65):
                g.append(67)
            elif(f[i]>122):
                g.append(113)
            else:
               g.append(e[i])
    for i in g:
        print(chr(i),end='')
    a-=1
    print("")
