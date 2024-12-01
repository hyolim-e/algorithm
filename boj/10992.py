import sys

N = int(input())

def print_top_line(N):
    top_line = (" " * (N - 1)) + "*"
    print(top_line)

def print_last_line(N):
    last_line = "*" * (2 * N - 1)
    print(last_line)
    return 0

def print_upper_lines(N):
    # N-M공백 1별 2(M-1)-1 1별
    for M in range(2, N):
        current_line = (" " * (N - M)) + "*" + (" " * (2 * (M-1) - 1)) + "*"
        print(current_line)
    return 0

def draw_tree(N):
    if N == 1:
        print("*")
    else:
        print_top_line(N)
        print_upper_lines(N)
        print_last_line(N)
    return 0

draw_tree(N)