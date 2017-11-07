import sys
str = sys.stdin.readline()
for i in range(len(str)):
    if str[i].islower():
        sys.stdout.write(str[i].upper())
    else:
        sys.stdout.write(str[i].lower())
