import math

t = int(input())

for k in range(t):
    
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()

    mis = 0
    mas = 0

    for i in range(0,n,2):
        mis += abs(arr[i] - arr[i+1])

    i = 0
    while(i < n/2):
        mas += abs(arr[i] - arr[n-i-1])
        i += 1

    print(mis,mas)
