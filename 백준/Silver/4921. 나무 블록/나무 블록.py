def main():
    d={'1':'45','2':'','3':'45','4':'23','5':'8','6':'23','7':'8','8':'67'}
    a=[]
    for i, j in enumerate(open(0),1):
        t=f'{i}. '
        j=j.strip()
        n=len(j)-1
        if j=='0':
            break
        if j[0]=='1' and j[-1]=='2':
            for k in range(n):
                if j[k+1] not in d[j[k]]:
                    t+='NOT'
                    break
            else:
                t+='VALID'
        else:
            t+='NOT'
        a.append(t)
    print('\n'.join(a))

if __name__ == "__main__":
    main()