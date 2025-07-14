def check(s):
    order = []
    for i in s:
        if i in ob:
            order.append(ob[i])
        elif i in cb:
            if not order or i != order[-1]:
                return 'no'
            else:
                order.pop()
    return 'yes' if not order else 'no'
        
ans = []
ob = {'(':')', '[':']'}
cb = [')', ']']
while '.'!=(s:= input()):
    ans.append(check(s))
print('\n'.join(ans))