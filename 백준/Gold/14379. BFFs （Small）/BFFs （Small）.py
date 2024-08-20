class Circle():
    def __init__(self, n, bff) -> None:
        self.n = n
        self.bff = bff
        self.circle = [0]*n
        self.v = [0]*n
        self.m = 0

    def check_circle(self, d):
        for i in range(d):
            if self.bff[self.circle[i]]!=self.circle[(i+1)%d] and self.bff[self.circle[i]]!=self.circle[(d+i-1)%d]:return False
        return True

    def not_bbf(self, i, j):
        return self.circle[i]!=self.bff[j] and self.bff[self.circle[i]]!=j

    def dfs(self, d):
        if d>self.m and self.check_circle(d):self.m=d
        if self.m==self.n:return
        for i in range(self.n):
            if self.v[i]:continue
            if d>=2 and self.not_bbf(d-1, i+1) and self.not_bbf(0, i+1) and self.not_bbf(0, self.circle[1]):continue
            self.v[i]=1
            self.circle[d]=i+1
            self.dfs(d+1)
            self.v[i]=0

a=open(0)
ans=[]
for i in range(int(next(a))):
    n=int(next(a))
    bff=[0]+[*map(int,next(a).split())]
    circle = Circle(n, bff)
    circle.dfs(0)
    ans.append(f'Case #{i+1}: {circle.m}')
print('\n'.join(ans))