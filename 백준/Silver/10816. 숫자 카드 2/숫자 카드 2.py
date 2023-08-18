import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int,input().split()))
M = int(input())
ints = list(map(int,input().split()))

answer = {}
for c in sorted(cards):
    if c in answer:
        answer[c] += 1
    else:
        answer[c] = 1

print(' '.join(str(answer[i]) if i in answer else '0' for i in ints))