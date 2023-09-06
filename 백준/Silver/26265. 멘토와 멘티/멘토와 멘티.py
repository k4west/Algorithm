import sys  
N = int(sys.stdin.readline())
li = []

for _ in range(N):
    li.append(sys.stdin.readline().strip().split())
li.sort(key=lambda x:x[1], reverse=True)
li.sort(key=lambda x:x[0])

for m in li:
    print(*m)