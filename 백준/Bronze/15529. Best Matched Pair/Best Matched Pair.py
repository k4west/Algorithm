def main():
    a = open(0)
    n = int(next(a))
    arr = sorted(map(int, next(a).split()), reverse=True)
    m = -1
    for i in range(n-1):
        a = arr[i]
        for j in range(i+1, n):
            b = arr[j]
            o = c = a*b
            d = c%10
            flag = True
            while (c:=c//10):
                if d-1 == c%10:
                    d -= 1
                else:
                    flag = False
                    break
            if flag and m < o:
                m = o
    print(m)
main()