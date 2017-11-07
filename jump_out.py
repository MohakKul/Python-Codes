from sys import stdin, stdout
n = int(stdin.readline())
arr = [int(x) for x in stdin.readline().rstrip().split()]
a = []
for i in range(n):
    if ((arr[i] + i + 1)>n):
        a.append(i+1)
stdout.write(str(min(a))+"\n")
