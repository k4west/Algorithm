import sys

def main():
    input = sys.stdin.readline
    ans = []
    for _ in range(int(input())):
        dep = input().strip()
        x1, y1, z1 = map(float, input().split())
        arr = input().strip()
        x2, y2, z2 = map(float, input().split())
        d = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
        if d * 1000 % 10 == 5.0:
            d += 0.01
        ans.append(f"{dep} to {arr}: {d:0.2f}")
    print("\n".join(ans))

main()