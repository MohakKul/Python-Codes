n = int(input())

arr = []

for i in range(n):
    
    a = input()
    s = int(a[0])

    for j in range(1,len(a),2):

        if (a[j] == '+'):
            s += int(a[j+1])

        elif (a[j] == '-'):
            s -= int(a[j+1])

    arr.append(s)

print(max(arr))
