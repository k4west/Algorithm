class Cart():
    def __init__(self, maze) -> None:
        INF = float('inf')
        self.answer = INF
        self.maze = maze
        self.n, self.m = len(maze), len(maze[0])
        self.d = ((1, 0), (-1, 0), (0, 1), (0, -1), (0, 0))
        s = {1:'rs', 2:'bs', 3:'rd', 4:'bd'}
        for i in range(self.n):
            for j in range(self.m):
                if (k:=maze[i][j]) in [1,2,3,4]:
                    s[k] = [i, j]
        rc, bc, self.rd, self.bd = s.values()
        rv, bv = [[0]*self.m for _ in range(self.n)], [[0]*self.m for _ in range(self.n)]
        rv[rc[0]][rc[1]], bv[bc[0]][bc[1]] = 1, 1
        self.dfs(rc, bc, rv, bv, 0)
        if self.answer==INF:
            self.answer = 0

    def dfs(self, rc, bc, rv, bv, c):
        if rc == self.rd and bc == self.bd:
            if self.answer > c:
                self.answer = c
            return
        for drn, drm in self.d:
            if 0<=(nrn:=rc[0]+drn)<self.n and 0<=(nrm:=rc[1]+drm)<self.m and (self.maze[nrn][nrm]==3 or not rv[nrn][nrm]) and self.maze[nrn][nrm]!=5:
                rv[nrn][nrm] = 1
                for dbn, dbm in self.d:
                    if drn==drm==dbn==dbm==0:
                        break
                    if 0<=(nbn:=bc[0]+dbn)<self.n and 0<=(nbm:=bc[1]+dbm)<self.m and (self.maze[nbn][nbm]==4 or not bv[nbn][nbm]) and self.maze[nbn][nbm]!=5 and not (nrn==nbn and nrm==nbm) and not (rc==[nbn, nbm] and bc==[nrn, nrm]):
                        bv[nbn][nbm] = 1
                        self.dfs([nrn, nrm], [nbn, nbm], rv, bv, c+1)
                        bv[nbn][nbm] = 0
                rv[nrn][nrm] = 0

def solution(maze):
    cart = Cart(maze)
    return cart.answer