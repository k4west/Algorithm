import sys
N, L, W, H = map(int, sys.stdin.readline().split())
left, right = 0, (L * W * H / N) ** (1 / 3)
for _ in range(50):
    mid = (left + right) / 2
    if (L // mid) * (W // mid) * (H // mid) < N:
        right = mid
    else:
        left = mid
print(f"{left:.9f}")