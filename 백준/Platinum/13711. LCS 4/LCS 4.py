import sys
from bisect import bisect_left
def main():
    input = sys.stdin.readline
    n = int(input())
    n1_idx = [0] * n
    for i, n in enumerate(map(int, input().split())):
        n1_idx[n-1] = i
    n2 = map(int, input().split())
    ans = [n1_idx[next(n2)-1]]
    for num in n2:
        idx = n1_idx[num-1]
        if ans[-1] < idx:
            ans.append(idx)
        else:
            ans[bisect_left(ans, idx)] = idx
    print(len(ans))
main()