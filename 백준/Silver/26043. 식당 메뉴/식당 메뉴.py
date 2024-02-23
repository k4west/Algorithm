import sys


def sol(li: list) -> str:
    return " ".join(map(str, sorted(map(int, li)))) or "None"


def main():
    input = sys.stdin.readline
    A, B, C, F = [], [], [], []

    for _ in range(int(input())):
        type_, *num = input().split()
        if type_ == "1":
            C.append(num)
        else:
            F.append(num[0])
    for i in range(n := len(F)):
        (a, b), f = C[i], F[i]
        if f == b:
            A.append(a)
        else:
            B.append(a)
    print("\n".join((sol(A), sol(B), sol((a for a, _ in C[n:])))))


if __name__ == "__main__":
    main()