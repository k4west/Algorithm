import sys
input = sys.stdin.readline

def setting():
    n = int(input())
    li = [0] * n
    li = list(map(int,input().split()))
    return n, li

N, cards = setting()
M, ints = setting()

answer = {}
for c in sorted(cards):
    if c in answer:
        answer[c] += 1
    else:
        answer[c] = 1

print(' '.join(str(answer[i]) if i in answer else '0' for i in ints))