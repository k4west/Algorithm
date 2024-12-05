def main():
    a = open(0).read().split('\n')
    t = []
    for i in a:
        if i == 'e/o/i':
            break
        for idx, (row, n) in enumerate(zip(i.split('/'), (5, 7, 5)), 1): 
            c = 0
            for j in row.split():
                f = False
                for k in j:
                    if k in 'aeiouy':
                        if not f:
                            c += 1
                            f = True
                    else:
                        f = False
            if c!=n:
                t.append(idx)
                break
        else:
            t.append('Y')
    print('\n'.join(map(str, t)))
main()