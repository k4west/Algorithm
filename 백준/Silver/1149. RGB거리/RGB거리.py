from sys import stdin
input = stdin.readline

def main():
    N = int(input())
    RGB = []
    costs = [[] for _ in range(N)]
    for _ in range(N):
        RGB.append(list(map(int, input().split())))
    
    costs[0] = RGB[0]
    order = [0, 1, 2]
    for i in range(1, N):
        cost = []
        for j in order:
            cost.append(min(costs[i-1][(j+1)%3], costs[i-1][(j+2)%3]) + RGB[i][j])
        costs[i] = cost
    print(min(costs[N-1]))


if __name__ == "__main__":
    main()