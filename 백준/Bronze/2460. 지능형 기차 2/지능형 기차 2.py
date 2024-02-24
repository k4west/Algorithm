import sys

input = lambda: map(int, sys.stdin.readline().split())
max_passenger, current = 0, 0
for _ in range(10):
    off_num, on_num = input()
    current += on_num - off_num
    if max_passenger < current:
        max_passenger = current
print(max_passenger)