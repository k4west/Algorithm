import sys

def manage(E, R, N, arr, n, current, v, i):
    for j in range(i+1, N+1):
        if j == i + n + 1:
            j == N
            break
        if arr[j] > v: break

    if j != N:
        tmp = current + (j - i) * R - E
        if tmp < 0: return 0
        elif tmp > current: return current
        return tmp
    return current

def main():
    input = sys.stdin.readline
    ans = []
    for x in range(int(input())):
        E, R, N = map(int, input().split())
        n, current = (E+R-1)//R, E
        if E < R: R = E
        arr, gain = list(map(int, input().split())) + [0], 0

        for i in range(N):
            v = arr[i]
            spent = manage(E, R, N, arr, n, current, v, i)
            gain += v * spent
            current += R - spent
            if current > E: current = E
        ans.append(f"Case #{x+1}: {gain}")
    print("\n".join(ans))
main()