n = int(input())

a = [int(x) for x in input().split()]

if(n == len(set(a))):
    print(1)

else:
    max = 0
    for i in range(n):
        for j in range(i,n):
            if(a[i]==a[j]):
                s = a[i:j+1]
                if(len(s)>max):
                    max = len(s)
    print(max)
