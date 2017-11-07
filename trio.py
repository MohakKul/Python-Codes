n,m = input().split()
n,m = int(n),int(m)
a = [int(x) for x in input().split()]
c = [0,0,0]
res = 0
for i in range(n):
   c[a[i]%3] += 1
res += (c[0] * (c[0]-1) * (c[0]-2))//6
res += (c[1] * (c[1]-1) * (c[1]-2))//6
res += ((c[2]*(c[2]-1)*(c[2]-2))//6)
res += c[0]*c[1]*c[2]
print(res)
