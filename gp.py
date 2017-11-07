from sys import stdin, stdout
n = int(stdin.readline())
n1=n
for i in range(n1):
    r,s,p = [int(x) for x in stdin.readline().rstrip().split()]
    n=0
    su=1
    arr=[]
    arr.append(1)
    for i in range(n,p):
        arr.append(((arr[n]*r)%p))
        su= sum(arr)%p
        n+=1
        if(su== s):
            stdout.write(str(n+1)+"\n")
            break
    if( n==p):
        stdout.write(str(-1)+"\n")
