from sys import stdin
input = stdin.readline

def main():
    N = range(int(input()))
    M = (0, 0, 0)
    m = (0, 0, 0)
    for _ in N:
        a, b, c = map(int, input().split())
        M = a + max(M[0], M[1]), b + max(M), c + max(M[1], M[2])
        m = a + min(m[0], m[1]), b + min(m), c + min(m[1], m[2])
    print(max(M), min(m))

if __name__ == "__main__":
    main()