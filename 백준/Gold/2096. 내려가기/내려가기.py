from sys import stdin
input = stdin.readline

def main():
    N = range(int(input()))
    M1, M2, M3 = 0, 0, 0
    m1, m2, m3 = 0, 0, 0
    for _ in N:
        a, b, c = map(int, input().split())
        M1, M2, M3 = a + max(M1, M2), b + max(M1, M2, M3), c + max(M2, M3)
        m1, m2, m3 = a + min(m1, m2), b + min(m1, m2, m3), c + min(m2, m3)
    print(max(M1, M2, M3), min(m1, m2, m3))

if __name__ == "__main__":
    main()