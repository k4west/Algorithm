def main():
    k = open(0)
    m2a = {}
    for _ in range(26):
        a, m = next(k).rstrip().split()
        m2a[m] = a
    s, p = map(int, next(k).split())
    t, b, m = map(int, next(k).split())
    _, code = next(k).rstrip().split()

    d = {'1'*s: '-', '1'*p: '.', '0'*t: '*', '0'*b: ' ', '0'*m: '\n'}
    d = sorted(([k, v] for k, v in d.items()), key=lambda x: -len(x[0]))
    for bi, mo in d:
        code = code.replace(bi, mo)
    code = code.replace('*', '')
    ans = []
    for mose in code.split('\n'):
        ans.append(''.join([m2a[m] for m in mose.split(' ')]))
    print(' '.join(ans))
main()