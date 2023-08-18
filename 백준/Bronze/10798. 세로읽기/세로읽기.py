import sys
from itertools import zip_longest

input = sys.stdin.readline

li = [[] for _ in range(5)]
for n in range(5):
    li[n] = list(input().strip())

# Transpose the input list
answer = [''.join(row) for row in zip_longest(*li, fillvalue='')]
print(*answer, sep="")
