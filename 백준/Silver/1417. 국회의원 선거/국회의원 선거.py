import sys


def main():
    input = lambda: int(sys.stdin.readline())
    N = input()
    Dasom = input()
    li = [input() for _ in range(N - 1)]
    for i in range(101):
        m, idx = 0, 0
        for j in range(N - 1):
            if m < (t := li[j]):
                m, idx = t, j
        if m < Dasom:
            print(i)
            return
        li[idx] -= 1
        Dasom += 1


if __name__ == "__main__":
    main()