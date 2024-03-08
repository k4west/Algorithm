import sys
L, R = map(int, sys.stdin.readline().split())
diff = (R - L) % 9
L %= 9
print((L * (diff + 1) + diff * (diff + 1) // 2) % 9)