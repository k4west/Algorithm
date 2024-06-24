def main():
    alp = [False]*26
    li = []
    t = 'N'
    for w in [*open(0)][1:]:
        alp[ord(w[0])-65] = True
        li.append(w.strip())
    for w in li:
        check = True
        for i in w:
            if not alp[ord(i)-65]:
                check = False
        if check:
            t = 'Y'
            break
    print(t)
main()