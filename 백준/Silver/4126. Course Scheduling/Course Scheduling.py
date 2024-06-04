def main():
    a=open(0);d={}
    for _,_,c in set(tuple(next(a).strip().split()) for _ in range(int(next(a)))):d[c]=d.get(c,0)+1
    print('\n'.join(sorted([f'{k} {v}' for k,v in d.items()])))
main()