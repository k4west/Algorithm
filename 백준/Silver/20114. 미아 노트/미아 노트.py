import sys
N, H, W = map(int,sys.stdin.readline().split())
li, result = [0]*H, []
for h in range(H):
    li[h] = sys.stdin.readline().strip()
for j in range(0,N*W,W):
    temp = []
    for i in range(0, H):
        temp.extend(li[i][j:j+W])
    result.append(max(temp))
print("".join(result))