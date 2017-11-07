n = int(input())
i,j,p = map(int,input().split())

arr = [ [0]*n for _ in range(n) ]

for a in range(n):
    for b in range(n):
        m = max(abs(i-a),abs(b-j))
        if(m<p):
            arr[a][b] = p-m

for a in range(n):
    for b in range(n):
        print(arr[a][b],end= ' ')
    print('')
        
        
