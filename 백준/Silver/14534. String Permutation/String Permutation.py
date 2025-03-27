from itertools import permutations
t = []
for i in range(int(input())):
    t.append(f"Case # {i+1}:")
    L = input()
    t.extend(["".join([L[j] for j in i]) for i in permutations(range(len(L)), len(L))])
print('\n'.join(t))