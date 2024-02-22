import sys
from collections import deque

def main():
    input = sys.stdin.readline
    A, B, C = [], [], deque([])
    for _ in range(int(input())):
        type_, *num = map(int, input().split())
        if type_ == 1:
            C.append(num)
        else:
            a, b = C.popleft()
            if num[0] == b:
                A.append(a)
            else:
                B.append(a)
    print(" ".join(map(str, sorted(A))) or "None")
    print(" ".join(map(str, sorted(B))) or "None")
    print(" ".join(map(str, sorted((a for a, _ in C)))) or "None")

if __name__ == "__main__":
    main()