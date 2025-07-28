string = input()
bomb = input()
stack = []
length = len(bomb)
cnt = 0

for s in string:
    stack.append(s)
    cnt += 1
    if cnt >= length:
        idx = 0
        while length >= 1-idx and stack[idx-1] == bomb[idx-1]:
            idx -= 1
        if length == -idx:
            for _ in range(length):
                stack.pop()
                cnt -= 1
print(''.join(stack) if stack else 'FRULA')