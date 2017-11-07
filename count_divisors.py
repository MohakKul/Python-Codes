from sys import stdin
a, b, c= [int(x) for x in stdin.readline().rstrip().split()]
d= []
for i in range(a,b+1):
    if (i%c==0):
        d.append(i)
print(len(d))