from collections import Counter
import sys

n = int(sys.stdin.readline())

a = []

for _ in range(n):

    i = int(sys.stdin.readline())

    a.append(i)
    
a = Counter(a)

q = int(sys.stdin.readline())

for _ in range(q):

    b = int(sys.stdin.readline())

    count = 0

    for key in a:

        if key%b == 0:

            count += a[key]

    sys.stdout.write(str(count)+"\n")
