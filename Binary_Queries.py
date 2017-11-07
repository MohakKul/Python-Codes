from sys import stdin, stdout
a,b = [int(i) for i in stdin.readline().split()]
c = stdin.readline().split()
while(b):
    q1= stdin.readline().split()
    if(int(q1[0])== 0):
        if(c[int(q1[2])-1]==0):
            print("EVEN")
        else:
            print("ODD")
    else:
        c[int(q1[1])-1]= 0 if c[int(q1[1])-1]== 1 else 1
    b-=1
