import sys

s = sys.stdin.readline().strip()

l = ['c=','c-','d-','lj','nj','s=','z=']

count = 0
i = 0

while s:
    if s[0:3] == 'dz=':
        count +=1
        s = s[3:]
    else:
        if s[0:2] in l:
            count +=1
            s = s[2:]
        else:
            count +=1
            s = s[1:]
print(count)