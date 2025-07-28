N = int(input())
*A, = map(int, input().split())
ans, stack = [], []
for a in A[::-1]:
    while stack and stack[-1] <= a:
        stack.pop()
    if not stack:
        ans.append(-1)
    else:
        ans.append(stack[-1])
    stack.append(a)
print(' '.join(map(str, ans[::-1])))