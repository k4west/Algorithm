def main():
    a, c, m, r0 = map(int, input().split())
    maxd = 0
    d = 0
    lb = 0
    ub = 1800000
    s = [0] * (ub + 1)  # ub를 포함하기 위해 +1
    while lb < m:
        s = [0] * (ub - lb + 1)  # ub를 포함하기 위해 +1
        r = r0
        if lb <= r <= ub:
            s[r - lb] = 1
        for i in range(1, m + 2):  # m+1 번 반복
            r = (a * r + c) % m
            if lb <= r <= ub:
                s[r - lb] = 1
        j = 0
        while j < len(s) and s[j] == 0:
            j += 1
        for i in range(j, len(s)):
            if s[i] == 1:
                if d > maxd:
                    maxd = d
                d = 1
            else:
                d += 1
        lb = ub + 1
        ub += len(s)
    print(maxd)
if __name__ == "__main__":
    main()