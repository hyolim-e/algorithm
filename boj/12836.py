import sys


N, num_query = map(int, sys.stdin.readline().split())

account = [0 for _ in range(N)]

for _ in range(num_query):
    case, p, q = map(int, sys.stdin.readline().split())
    
    if case == 1:
        account[p-1] += q
    
    if case == 2:
        balance = sum(account[p-1:q])
        print(balance)