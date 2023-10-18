from sys import stdin
input = stdin.readline

def main():
    N = int(input())
    RGB = []
    for _ in range(N):
        RGB.append(list(map(int, input().split())))
    
    for i in range(1, N):
        for j in range(3):
            RGB[i][j] += min(RGB[i-1][(j+1)%3], RGB[i-1][(j+2)%3])
    print(min(RGB[N-1]))


if __name__ == "__main__":
    main()