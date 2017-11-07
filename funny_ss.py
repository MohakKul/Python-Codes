import sys
N = sys.stdin.readline()
N = int(N)
A = [int(x) for x in sys.stdin.readline().split()]
flag = True
for i in range(N-1, 0, -1):
    try:
        for j in range(N-i):
            if A[j] == A[j+i]:
                sys.stdout.write(str(i+1))
                flag = False
                raise NameError
    except:
        break

if flag:
    sys.stdout.write('0')
