def is_palindrome(s):
    for i in range((n:=len(s))-1): 
        if s[i] == s[i+1] or (i+2 != n and s[i] == s[i+2]): return True
    return False
p = q = 0
for i in range(int(next(a:= open(0)))):
    s = next(a)
    if is_palindrome(s): p += 1
    elif is_palindrome(s.replace('j', 'i').replace('b', 'p').replace('d', 'p')): q += 1
print(f'{p}\n{p+q}')