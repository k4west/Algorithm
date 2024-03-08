import sys
input = sys.stdin.readline
rooms = [1 for _ in range(int(input()))]
for _ in range(int(input())):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(x, y): rooms[i] = 0
print(sum(rooms))