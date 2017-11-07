import math
import functools
def factors(n):
        step = 2 if n%2 else 1
        return set(functools.reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(math.sqrt(n))+1, step) if n % i == 0)))
 
 
for _ in range(int(input())):
    l=list(map(int,input().split()))
    list1=factors(l[0])
    list2=factors(l[1])
    list3=list(set(list1).intersection(list2))
    list3=set(list3)
    list3=list(list3)
    list3.sort(reverse=True)
    if len(list3)>=l[2]:
        print(list3[l[2]-1])
    else:
        print('No crymeth today')
