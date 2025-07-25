from sys import stdin
input = stdin.readline

N = int(input())
stack = []
ans = []
for _ in range(N):
    a, *b = map(int, input().split())
    if a == 1:
        stack.append(b[0])
    elif a == 2:
        ans.append(stack.pop() if stack else -1)
    elif a == 3:
        ans.append(len(stack))
    elif a == 4:
        ans.append(1-bool(stack))
    elif a == 5:
        ans.append(stack[-1] if stack else -1)
print('\n'.join(map(str, ans)))