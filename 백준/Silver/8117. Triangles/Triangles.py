ds = sorted(map(int, open(0).read().split()), reverse=True)
n = len(ds)
for i in range(n-2):
    if ds[i] < sum(ds[i+1:i+3]):
        print(' '.join(map(str, ds[i:i+3])))
        break
else:
    print('NIE')