import sys
input = sys.stdin.readline
ans= 10000

def main():
    N, M = map(int, input().split())
    town = [input().rstrip().split() for _ in range(N)]
    houses, chicken = [], []
    nc = 0

    for i in range(N):
        for j in range(N):
            if town[i][j] == '2':
                chicken.append((i, j))
                nc += 1

    for r1 in range(N):
        for c1 in range(N):
            if town[r1][c1] == '1':
                tmp = []
                for r2, c2 in chicken:
                    tmp.append(abs(r2-r1)+abs(c2-c1))
                houses.append(tmp)

    visited = [False] * nc
    def distance():
        indices = [i for i in range(nc) if visited[i]]
        s_dist = 0
        for house in houses:
            dist = 100
            for idx in indices:
                if house[idx] < dist:
                    dist = house[idx]
            s_dist += dist        
        return s_dist

    def dfs(n, idx):
        global ans
        if n == M:
            s_dist = distance()
            if s_dist < ans: ans = s_dist
        
        for i in range(idx, nc):
            if not visited[i]:
                visited[i] = True
                dfs(n+1, i)
                visited[i] = False

    dfs(0, 0)
    print(ans)

if __name__ == "__main__":
    main()