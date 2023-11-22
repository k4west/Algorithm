string = input()
bomb = input()
b = len(bomb)

stack = []
for s in string:
    stack.append(s)
    if "".join(stack[-b:]) == bomb:
        for _ in range(b):
            stack.pop()

print("".join(stack) if stack else "FRULA")