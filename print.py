n = int(input())

st = input()

co = 0

h = st.count('h')
a = st.count('a')
c = st.count('c')
k = st.count('k')
e = st.count('e')
r = st.count('r')
t = st.count('t')

while(1):
    if((h==0)or(a==0)or(c==0)or(k==0)or(e==0)or(r==0)or(t==0)or(h==1)or(a==1)or(e==1)or(r==1)):
        break
    h -= 2
    a -= 2
    e -= 2
    r -= 2
    c -= 1
    k -= 1
    t -= 1
    co += 1

print(c)
