def main():
    import sys

    input = sys.stdin.readline
    N = int(input())
    s = [0] * 10001
    for _ in range(N): s[n := int(input())] += 1
    for i, n in enumerate(s):
        if n:
            i = str(i)
            for _ in range(n): sys.stdout.write(i + "\n")

if __name__ == "__main__":
    main()