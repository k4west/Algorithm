def main():
    a = [*map(int, open(0).read().split())]
    s = sum(a) - 100
    for i in range(8):
        t = a[i]
        for j in range(i+1, 9):
            if t+a[j] == s:
                print(*[a[k] for k in range(9) if k !=i and k != j], sep='\n')
                return
main()