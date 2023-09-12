a = open(0)
next(a)
P = [1, 1, 1, 2, 2]
for _ in range(95):
    P.append(P[-1] + P[-5])
for n in a:
    print(P[int(n)-1])