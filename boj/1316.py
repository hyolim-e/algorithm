import sys

n = int(sys.stdin.readline().strip())

answer = 0

for i in range(n):
    word = sys.stdin.readline().strip()
    is_group = True
    visited = []
    last_s = None
    for s in word:
        if last_s is None:
            last_s = s
            visited.append(s)
            continue
        if last_s == s:
            continue
        else:
            if s in visited:
                is_group = False
                break
            else:
                visited.append(s)
                last_s = s
                continue
    answer += is_group
            
print(answer)