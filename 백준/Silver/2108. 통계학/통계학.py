import sys
import statistics as st
input = sys.stdin.readline

N = int(input())
P = [0] * N
for n in range(N):
    P[n] = int(input())

mli = st.multimode(P)
mli.sort()
P.sort()

print(round(sum(P) / N))
print(P[N // 2])
print(mli[1] if len(mli) > 1 else mli[0])
print(P[N-1] - P[0])