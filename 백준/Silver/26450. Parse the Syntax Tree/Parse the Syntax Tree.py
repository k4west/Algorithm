def parse(a, x, y, w):
    if w == 1: return a[x][y]
    for i in range(w):
        if a[x][y + i] in '+-*':
            op = a[x][y + i]
            break
    left = parse(a, x + 1, y, i)
    right = parse(a, x + 1, y + i + 1, w - i - 1)
    return str(eval(''.join((left,op,right))))

def main():
    n,*a=open(0)
    _,W=map(int,n.split())
    print(parse(a, 0, 0, W))

if __name__ == "__main__":
    main()