def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True


n = int(input())

arr = []

for i in range(n):
    arr.append(list(map(int,input().split())))
    
count = 0

for i in range(n):
    for j in range(n):
        s = 0
        top = 1
        bottom = 1
        left = 1
        right = 1
        if(i == 0): top = 0
        if(i == n-1): bottom = 0
        if(j == 0): left = 0
        if(j == n-1): right = 0

        if(top != 0):
            s += arr[i-1][j]
        if(bottom != 0):
            s += arr[i+1][j]
        if(left != 0):
            s += arr[i][j-1]
        if(right != 0):
            s += arr[i][j+1]

        if(is_prime(s)):
            count += 1

print(count)
        


