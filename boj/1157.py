import sys

s = sys.stdin.readline().strip()
s = s.upper()

d = {}

for char in s:
    if d.get(char):
        d[char] +=1
    else:
        d[char] = 1

m = max(d.values())
answer = None

for k, v in d.items():
    if v == m:
        if answer==None:
            answer = k
        else:
            answer = '?'

print(answer)