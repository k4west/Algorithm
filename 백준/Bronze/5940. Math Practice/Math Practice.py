A, B = input().split()
E = 0
for e in range(int(A) + 1, 63):
    if f"{1 << e}"[0] == B: E = e; break
print(E)