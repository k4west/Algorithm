from sys import stdin
input = stdin.readline
input()
*li, = map(int, input().split())
n = 1
stack = []
for i in li:
    if i == n:
        n += 1
        while stack and n == stack[-1]:
            stack.pop()
            n += 1
    elif not stack or stack[-1] > i:
        stack.append(i)
    else:
        break
print('Sad' if stack else 'Nice')
