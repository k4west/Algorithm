import sys
input = sys.stdin.readline
def p(i, n):
    while n >= 2000:
        sys.stdout.write(f"{i}\n" * 2000)
        n -= 2000
    if n:
        sys.stdout.write(f"{i}\n" * n)
def main():
    N = int(input())
    s = [0] * 10001
    for _ in range(N): s[n := int(input())] += 1
    for i, n in enumerate(s): p(i, n)
if __name__ == "__main__":
    main()