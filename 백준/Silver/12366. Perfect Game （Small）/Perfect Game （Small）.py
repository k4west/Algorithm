import sys
input = sys.stdin.readline
for i in range(int(input())):
    N = int(input())
    input()
    print(f"Case #{i+1}: {' '.join((j for _, j in sorted(list(zip(map(int, input().split()), map(str, range(N)))), key=lambda x: -x[0])))}")