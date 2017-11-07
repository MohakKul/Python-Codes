a= int(input())
while(a):
    b= int(input())
    c= input()
    c=c+"m"
    count1= 0
    count2=0
    for i in range (len(c)):
        if(c[i].isdigit()):
            count1+=1
        else:
            if(count1>=1):
                count2+=1
                count1=0
    print (count2)
    a-=1
