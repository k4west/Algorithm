from sys import stdin
from collections import deque
input = stdin.readline

def main():
    A, B = map(int, input().split())

    q = deque([A])
    nq = deque()
    c = 1
    while q or nq:
        if not q:
            q, nq = nq, q
            c += 1
        n = q.popleft()
        for m in (2*n, 10*n+1):
            if m == B:
                print(c+1)
                return
            if m < B:
                nq.append(m)
    print("-1")

if __name__ == "__main__":
    main()