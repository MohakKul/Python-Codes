n=int(input())
arr1= ['W','W', 'M', 'A', 'A', 'M', 'W', 'W', 'M', 'A', 'A', 'M']
arr2= [-11, 11, 9, 7, 5, 3, 1, -1, -3, -5, -7, -9 ]
sol1=[]
sol2=[]
for i in range(n):
    seat=int(input())
    key=seat%12
    sol1.append(arr1[key])
    sol2.append(seat+arr2[key])
for i in range(n):
    print(sol2[i],sol1[i]+"S")
    
