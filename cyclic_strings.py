t = int(input())

arr = list(map(int,input()))

rot = 0

while(len(arr)>0):
    arr = arr[-1:] + arr[:-1]
    rot += 1
    if(rot == len(arr)):
        arr.pop(len(arr)//2)

print(rot)
