def f(n):
    s = 0
    for i in range(1, int(n**.5)+1):
        if n % i == 0: 
            s += i
            if i != (j:=n//i): s += j
    return ('Deficient', 'Abundant')[2*n < s]
ans = []
input()
for n in map(int, input().split()):
    if n in {6,28,496,8128}: ans.append("Perfect")
    else: ans.append(f(n))
print("\n".join(ans))