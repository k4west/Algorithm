def main():
    N, M, *arr = map(int, open(0).read().split())
    r = [0 for _ in range(M)]
    s = 0
    for a in arr: s = (s+a)%M; r[s] += 1
    print(r[0] + sum(r[i]*(r[i]-1)//2 for i in range(M)))
main()