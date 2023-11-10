string = input()
n_string = ""
stack = []

for s in string:
    if s in ('+', '-'):
        while stack and stack[-1] != '(':
            n_string += stack.pop()
        stack.append(s)
    elif s in ('*', '/'):
        while stack and stack[-1] in ('*', '/'):
            n_string += stack.pop()
        stack.append(s)
    elif s == '(':
        stack.append('(')
    elif s == ')':
        while stack and stack[-1] != '(':
            n_string += stack.pop()
        stack.pop()
    else:
        n_string += s

while stack:
    n_string += stack.pop()
print(n_string)