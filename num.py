from sys import stdin, stdout

n,q = [int(c) for c in input().split()]
 
arr = [int(x) for x in stdin.readline().split()]
 
a = []
 
a.append(0)
a.append(arr[0])
 
for i in range(2,n+1):
    a.append(a[i-1] + arr[i-1])
 
for i in range(q):
    l,r = [int(c) for c in input().split()]
    z = a[r] - a[l-1]
    x = r-l+1
    stdout.write(str(z//x)+"\n")
