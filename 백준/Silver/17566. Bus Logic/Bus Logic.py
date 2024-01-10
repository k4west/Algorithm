import sys

input = sys.stdin.readline
m, b, s = map(int, input().split())
routes = [list(map(int, input().rstrip())) for _ in range(b)]
reachable_stops = [0] * s
m -= 1
for route in routes:
    if not route[m]:
        continue
    for idx, stop in enumerate(route):
        reachable_stops[idx] |= stop
reachable_stops[m] = 0
print(sum(reachable_stops))