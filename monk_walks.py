a=int(input())
for j in range(a):
    b=input()
    vowels= ['A','E','I','O','U','a','e','i','o','u']
    count=0
    for i in vowels:
        count+=b.count(i)
    print(count)
    
