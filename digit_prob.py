import sys

a = sys.stdin.readline().split()

x = list(a[0])
k = int(a[1])
i = 0

while (i<k):
    
    if (x[i] != '9'):
        x[i] = '9'

    else:
        k += 1
    i += 1
        
sys.stdout.write("".join(x))
