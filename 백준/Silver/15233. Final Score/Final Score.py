f=lambda:input().split()
def main():
    d,s={},0
    for n in f():d[n]=1
    for n in f():d[n]=-1
    for n in f():s+=d[n]
    if s:s//=abs(s)
    print(['TIE','A','B'][s])
input()
main()