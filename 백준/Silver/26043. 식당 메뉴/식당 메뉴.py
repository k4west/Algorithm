import sys
from collections import deque
def sol(li):return " ".join(map(str,sorted(li))) or "None"
def main():
    input = sys.stdin.readline
    A, B, C = [], [], deque([])
    for _ in range(int(input())):
        type_, *num = input().split()
        if type_ == '1': C.append(num)
        else:
            a, b = C.popleft()
            if num[0] == b: A.append(int(a))
            else: B.append(int(a))
    print("\n".join((sol(A),sol(B),sol(map(int,(a for a,_ in C))))))
if __name__ == "__main__":main()