t= int(input())
for i in range(t):
    n=int(input())
    for j in range (0,1000):
        if(n<=(pow(2,j))):
            print(j)
            break
        elif(n>pow(2,j)):
            continue
