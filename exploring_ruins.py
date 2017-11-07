import sys
s = list(sys.stdin.readline())
for i in range(len(s)):
    if(s[i] == '?' and len(s) == 1):
        s[i] = 'a'
    elif (s[i] == '?'):
        if (i == 0 and (s[i+1] == '?' or s[i+1] == 'b')):
            s[i] = 'a'
        elif (i == len(s)-1 and (s[i-1] == '?' or s[i-1] == 'b')):
            s[i] = 'a'
        elif((s[i-1] == 'b' or s[i-1] == '?') and (s[i+1] == '?' or s[i+1] == 'b')):
            s[i] = 'a'    
        else:
            s[i] = 'b'
sys.stdout.write("".join(str(x) for x in s))
