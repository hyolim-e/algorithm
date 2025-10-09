import sys
import heapq

s = sys.stdin.readline()

queue = []

for i in range(len(s)):
    heapq.heappush(queue, (s[i:],i))

for _ in range(len(queue)):
    str, idx = heapq.heappop(queue)
    print(idx)