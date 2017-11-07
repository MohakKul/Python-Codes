import sys

n = sys.stdin.readline()

a = [int(x) for x in sys.stdin.readline().split()]

pr = 1

for i in a:
    pr = (pr*i)%(10**9 +7)
    
sys.stdout.write(str(pr))
