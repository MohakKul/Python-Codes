t = int(input())

for _ in range(t):
    
    n = int(input())
    
    arr = [int(x) for x in input().split()]
    
    count = 1
    max_speed = arr[0]
    
    if (n==1 or n==0):
        print(n)
        
    else:
        for i in range(n-1):
            if(arr[i+1]<=max_speed):
                count += 1
                max_speed = arr[i+1]
                
        print(count)
