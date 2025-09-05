from collections import deque
from sys import stdin
input = stdin.readline

n, w, L = map(int, input().split())
t = 0
cnt = on_bridge = 0
bridge = deque([])
for truck in map(int, input().split()):
    t += 1
    if cnt and bridge[0][1] == t:
        prev_truck, t = bridge.popleft()
        on_bridge -= prev_truck
        cnt -= 1

    while on_bridge + truck > L or cnt == w:
        prev_truck, t = bridge.popleft()
        on_bridge -= prev_truck
        cnt -= 1

    bridge.append((truck, t+w))
    cnt += 1
    on_bridge += truck

if cnt:
    _, t = bridge.pop()
print(t)