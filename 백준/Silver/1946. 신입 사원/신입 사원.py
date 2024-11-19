def main():
    a = open(0)
    t = []
    for _ in range(int(next(a))):
        c = 1
        n = int(next(a))
        li = [0] * (n+1)
        for _ in range(n):
            i, j = map(int, next(a).split())
            li[i] = j
        m = li[1]
        for i in range(2, n+1):
            if m > (j:=li[i]):
                c += 1
                m = j
        yield(c)

def sol():
    for i in main():
        print(i)
sol()