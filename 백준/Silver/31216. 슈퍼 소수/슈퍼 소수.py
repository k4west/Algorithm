import sys
input = sys.stdin.readline
def is_prime():
    N = 318137
    ps = [False, False] + [True] * (N - 1)
    for i in range(2, int(N**0.5) + 1):
        if ps[i]:
            for j in range(i * i, N + 1, i):
                ps[j] = False
    return ps
def main():
    primes = [0] + [p for p, v in enumerate(is_prime()) if v]
    ans = []
    for _ in range(int(input())):
        ans.append(primes[primes[int(input())]])
    print("\n".join(map(str, ans)))
main()