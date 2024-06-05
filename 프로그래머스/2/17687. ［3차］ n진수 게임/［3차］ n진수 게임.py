d={i:s for i,s in zip(range(16),'0123456789ABCDEF')}
def solution(n, t, m, p):
    s='0';i=0
    while len(s)<t*m:
        i+=1;v=[];j=i
        while j:v.append(j%n);j//=n
        s+=''.join(map(lambda x:d[x],v[::-1]))
    return ''.join(s[p-1::m][:t])