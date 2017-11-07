seg = {'0': 6, '1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 7, '8' : 7, '9' : 6}

def calc(n):
    res = 0
    for a in n:
        res += seg[a]
    return res
    
t = int(input())

for i in range(t):
    
    l = int(input())

    arr = input().split()
    
    result = arr[0]
    best_bulbs = calc(result)
    
    for j in arr:        
        new = calc(j)    
        if new < best_bulbs:            
            best_bulbs = new
            result = j
        if j == '1':
            result = '1'
            break
        
    print(result)
            
