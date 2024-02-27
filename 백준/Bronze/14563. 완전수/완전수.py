import sys
input = sys.stdin.readline
def Aliquot_sum(n):
    s = 0
    for i in range(1, n):
        if n % i == 0: s += i
    return s
ans = []
input()
for n in map(int, input().split()):
    if n == (a := Aliquot_sum(n)): ans.append("Perfect")
    elif n > a: ans.append("Deficient")
    else: ans.append("Abundant")
print("\n".join(ans))