from sys import stdin
input = stdin.readline

def main():
    N = int(input())
    RGB = [(0,0,0)]
    for i in range(N):
        r, g, b = map(int, input().split())
        RGB.append((r + min(RGB[i][1], RGB[i][2]), g + min(RGB[i][2], RGB[i][0]), b + min(RGB[i][0], RGB[i][1])))
    print(min(RGB[N]))


if __name__ == "__main__":
    main()