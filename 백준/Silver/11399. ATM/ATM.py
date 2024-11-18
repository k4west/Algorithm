a = open(0)
N = int(next(a))
print(sum([t*(N-i) for i, t in enumerate(sorted(map(int, next(a).split())))]))