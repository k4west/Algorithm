def preprocess(t):
    s=''
    for i in t.upper():
        if ord(i) in range(65, 91):s+=i
        else: s+=' '
    return s

def multiset_count(t):
    s=preprocess(t)
    d={}
    for i in range(len(s)-1):
        t=s[i:i+2]
        if ' ' not in t:d[t]=d.get(t,0)+1
    return d

def solution(str1, str2):
    s1, s2 = multiset_count(str1), multiset_count(str2)
    M = sum((max(s1.get(s,0),s2.get(s,0)) for s in set(s1.keys()) | set(s2.keys())))
    m = sum((min(s1[s],s2[s]) for s in set(s1.keys()) & set(s2.keys())))
    if M:return (m/M)*65536//1
    else: return 65536