from itertools import combinations
def main():
    N = int(input())
    factorials = [1]
    i = 1
    while (t:=factorials[-1]*i) < N:
        factorials.append(t)
        i += 1
    if factorials[-1]*i == N:
        return 'YES'
    for i in range(1, len(factorials)+1):
        for cb in combinations(factorials, i):
            if sum(cb) == N:
                return 'YES'
    return 'NO'
print(main())