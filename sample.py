num=int(input())
c=0
for i in range(100):
    if (int(abs(pow(2,c)-num)))>(int(abs(pow(2,i)-num))):
        c=i
print (int(abs(pow(2,c)-num)))
