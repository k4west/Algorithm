import sys
def main():
    input = sys.stdin.readline
    ans = []
    for x in range(int(input())):
        E, R, N = map(int, input().split())
        n = (E+R-1)//R
        current = E
        if E < R:
            R = E
        arr = list(map(int, input().split())) + [0]
        gain = 0

        for i in range(N):
            v = arr[i]
            for j in range(i+1, N+1):
                if j == i + n + 1:
                    j == N
                    break
                if arr[j] > v:
                    break

            if j == N:
                spent = current
            else:
                tmp = current + (j - i) * R - E
                if tmp < 0:
                    tmp = 0
                elif tmp > current:
                    tmp = current
                spent = tmp

            gain += v * spent
            current += R - spent
            if current > E:
                current = E

        ans.append(f"Case #{x+1}: {gain}")
    print("\n".join(ans))
main()