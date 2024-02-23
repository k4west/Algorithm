import sys

input = sys.stdin.readline
n = int(input())
hs = map(int, input().split())
t = int(input())
best_setting, waste = 0, t
for h in hs:
    w = t % h
    if waste > w:
        waste, best_setting = w, h
print(best_setting)