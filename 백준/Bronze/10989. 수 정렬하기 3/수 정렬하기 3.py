import sys
input = sys.stdin.readline
print = sys.stdout.write
def p(i, n):
    while n >= 3000:
        print(f"{i}\n" * 3000)
        n -= 3000
    if n: print(f"{i}\n" * n)
def main():
    N = int(input())
    s = [0] * 10001
    for _ in range(N): s[n := int(input())] += 1
    for i, n in enumerate(s): p(i, n)
if __name__ == "__main__":
    main()