N= int(input())
for i in range(N):
    n= input()
    print("The streak is broken!") if ('21' in n) or (int(n))%21==0 else print ("The streak lives still in our heart!")
