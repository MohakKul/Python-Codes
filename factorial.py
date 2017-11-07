days = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
n = int(input())
while(n):
    n1= int(input())
    arr = list(map(int,input().split()))
    arr2=[]
    for position,item in enumerate(arr):
        if item ==1:
            arr2.append(position)
    print(days[max(arr2)])
    n-=1
