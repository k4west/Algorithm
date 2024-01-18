import sys


def main():
    input = lambda: int(sys.stdin.readline())
    N = input()
    Dasom = input()
    li = [input() for _ in range(N - 1)] + [0]
    for i in range(101):
        if (m := max(li)) < Dasom:
            print(i)
            return
        li[li.index(m)] -= 1
        Dasom += 1


if __name__ == "__main__":
    main()