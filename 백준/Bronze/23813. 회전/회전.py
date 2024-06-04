def main():
    n=input();l=[n]
    while True:
        n=n[-1]+n[:-1]
        if l[0]==n:break
        l.append(n)
    print(eval('+'.join(l)))
main()