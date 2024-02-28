import sys

def main():
    input = lambda: set(map(int, sys.stdin.readline().split()))
    input()

    def sol(arr1, arr2):
        arr1 = list(arr1)
        arr1.sort()
        m_dist = 100_000_000
        for a in arr2:
            l, r = 0, len(arr1) - 1
            while l <= r:
                m = (l + r) // 2
                dist = abs(arr1[m] - a)
                m_dist = min(m_dist, dist)
                if arr1[m] < a: l = m + 1
                elif arr1[m] > a: r = m - 1
                else: return 0
        return m_dist

    print(sol(input(), input()))

if __name__ == "__main__":
    main()