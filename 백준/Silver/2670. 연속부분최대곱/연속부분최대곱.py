N = int(input())
fs = [float(input()) for _ in range(N)] + [0]
for i in range(N):
    if fs[i] < (t:=fs[i] * fs[i-1]):
        fs[i] = t
print(f"{max(fs):.3f}")