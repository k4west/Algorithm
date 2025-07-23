A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
t = 0
if A < 0:
    t -= A*C
    A = 0
if A == 0:
    t += D
t += (B - A) * E
print(t)
