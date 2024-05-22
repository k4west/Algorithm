h1={2:[1], 5:[2], 6:[0]}
h2={2:[1], 3:[7], 4:[4], 5:[2,3,5], 6:[0,6,9], 7:[8]}
h={}
for n1 in h1:
    for n2 in h2:
        for s in h1[n1]:
            for t in h2[n2]:
                if not (s==2 and t>=4):
                    if n1+n2 not in h: h[n1+n2]=[]
                    h[n1+n2].append(s*10+t)                  
m1={2:[1], 4:[4], 5:[2,3,5], 6:[0]}
m2={2:[1], 3:[7], 4:[4], 5:[2,3,5], 6:[0,6,9], 7:[8]}
m={n1+n2:[s*10+t for s in m1[n1] for t in m2[n2]] for n1 in m1 for n2 in m2}
m={}
for n1 in m1:
    for n2 in m2:
        for s in m1[n1]:
            for t in m2[n2]:
                if n1+n2 not in m: m[n1+n2]=[]
                m[n1+n2].append(s*10+t) 
n = int(input())
if 8<=n<=26:
    for i in h:
        if n-i in m:
            print(f'{h[i][0]:02d}:{m[n-i][0]:02d}')
            break
else:
    print('Impossible')