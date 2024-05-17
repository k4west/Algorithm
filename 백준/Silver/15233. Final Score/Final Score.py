def main():
    a=open(0)
    next(a)
    dic={}
    s=0
    for name in next(a).strip().split():dic[name]=1
    for name in next(a).strip().split():dic[name]=-1
    for name in next(a).strip().split():s+=dic[name]
    if s:s//=abs(s)
    print(['TIE','A','B'][s])
main()