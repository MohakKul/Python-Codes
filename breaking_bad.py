from sys import stdin
d= int(input())
for i in range(d):
    x,y,k= [int(i) for i in stdin.readline().split()]
    arr=[]
    for j in range(min(x,y)+1,0,-1):
        if((x%j==0) and (y%j==0)):
            arr.append(j)
    print(arr)
    """if(len(arr)<k):
        print("No crymeth today")
    else:
        print(arr[k-1])"""
