n = int(input())

d = {}

for _ in range(n):

    a,b = input().split()
    d[a] = b

s= list(input())

for i in s:
    try:
        s[i]= d[i]
    except:
        continue

print(*s)
