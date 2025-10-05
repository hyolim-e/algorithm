import sys

n, m = map(int, sys.stdin.readline().strip().split(' '))

baskets = list(range(1,n+1))

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split(' '))
    for i in range((b-a+1)//2):
        baskets[a-1+i], baskets[b-1-i] = baskets[b-1-i], baskets[a-1+i]

for basket in baskets:
    print(basket)