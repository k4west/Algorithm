d = [119, 218, 320, 419, 520, 621, 722, 822, 922, 1022, 1122, 1221]
def f(n):
    for i in range(12):
        if n <= d[i]:
            return i
    return 0

def main():
    a = open(0)
    v = set()
    t = []
    for _ in range(7):
        k = int("".join(map(lambda x: x.strip().zfill(2), next(a).split())))
        v.add(f(k))
    for _ in range(int(next(a))):
        k = int("".join(map(lambda x: x.strip().zfill(2), next(a).split())))
        if f(k) not in v:
            t.append(k)
    t.sort()
    print('\n'.join(map(lambda x: f'{x//100} {x%100}', t)) if t else "ALL FAILED")
main()