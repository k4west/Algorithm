import sys
from collections import deque
def check(num):
    li = [i for i, j in enumerate(num) if j]
    return li[-1] - li[0]
def main():
    input = sys.stdin.readline
    input()
    num = [0] * 11
    q = deque([])
    ans = 1
    for a in map(int, input().split()):
        q.append(a)
        num[a] += 1
        while check(num) > 2: num[q.popleft()] -= 1
        if ans < (t := len(q)): ans = t
    print(ans)
main()