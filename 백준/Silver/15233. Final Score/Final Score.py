def main():
    dic,s={},0
    for name in input().split():dic[name]=1
    for name in input().split():dic[name]=-1
    for name in input().split():s+=dic[name]
    if s:s//=abs(s)
    print(['TIE','A','B'][s])
input()
main()