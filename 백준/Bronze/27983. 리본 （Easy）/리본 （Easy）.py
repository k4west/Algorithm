def main():
    n=int(input())
    *x,=map(int, input().split())
    *l,=map(int, input().split())
    *c,=input().split()
    for i in range(n):
        for j in range(i+1, n):
            if c[i]!=c[j] and x[j]-x[i]<=l[i]+l[j]:
                print('YES')
                print(i+1, j+1)
                return
    print('NO')
main()