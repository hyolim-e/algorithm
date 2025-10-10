import sys

s = sys.stdin.readline().strip().upper()
char_count = {}

for char in s:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

max_count = max(char_count.values())
answer = None

for k, v in char_count.items():
    if v == max_count:
        if answer is None:
            answer = k
        else:
            answer = '?'
print(answer)