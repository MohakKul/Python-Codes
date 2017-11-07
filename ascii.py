T = int(input())
 
primes = {2,3}
 
def isPrime(start, end):
    for i in range(start, end + 1):
        foundprime = True
        for n in primes:
            if i % n == 0:
                foundprime = False
                break
        if foundprime:
            primes.add(i)
 
def primeASCII():
    start = max(primes) + 2
    end = ord('z')
    isPrime(start, end)
    
    
def findNearestPrimeASCII(s):
    primelist = list(primes)
    primelist.sort()
    start = primelist.index(67)
    primelist = primelist[start:]
    word = ""
    for ch in s:
        dist = [abs(ch - i) for i in primelist]
        mindist = min(dist)
        minidx = dist.index(mindist)
        word += chr(primelist[minidx])
    
    return word
    
primeASCII()
        
for i in range(T):
    l = int(input())
    s = list(map(ord, input()))    
    print(findNearestPrimeASCII(s))