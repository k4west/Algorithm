n, k, *a = map(int, open(0).read().split())
a.sort()
print(sum(a[-k:]))