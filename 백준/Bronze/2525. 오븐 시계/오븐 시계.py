H, M = map(int, input().split())
m = int(input())
H += (m+M) // 60
M = (m+M) % 60
print(H%24, M)