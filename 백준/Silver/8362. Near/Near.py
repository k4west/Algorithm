import sys

def main():
    input = lambda: set(map(int, sys.stdin.readline().split()))
    input()

    def sol(arr1, arr2):
        if arr1 & arr2:
            return 0
        arr1 = list(arr1)
        arr1.sort()
        R = len(arr1) - 1
        m_dist = 100_000_000
        for a in arr2:
            l, r = 0, R
            while l <= r:
                m = (l + r) // 2
                if (t:= arr1[m]) < a: 
                    l = m + 1
                    dist = a - t
                    if m_dist > dist: m_dist = dist
                elif t > a: 
                    r = m - 1
                    dist = t - a
                    if m_dist > dist: m_dist = dist
        return m_dist

    print(sol(input(), input()))

if __name__ == "__main__":
    main()