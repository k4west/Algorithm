import sys
input = sys.stdin.readline
ans = []
while True:
    k, *m = list(map(int, input().split()))
    if k == 0:
        break
    chosen = set(map(int, input().split()))
    flag = True
    for _ in range(*m):
        _, r, *courses = list(map(int, input().split()))
        if flag and sum(course in chosen for course in courses) < r:
            flag = False
    ans.append("yes" if flag else "no")
print("\n".join(ans))