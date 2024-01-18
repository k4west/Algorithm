import sys

input = sys.stdin.readline
n = int(input())
professors = list(range(1, n + 1))
li = list(map(int, input().split()))
idx = 0
while n > 1:
    idx += li[idx] - 1
    idx %= n
    professors.pop(idx)
    li.pop(idx)
    n -= 1
    idx %= n
print(professors[0])