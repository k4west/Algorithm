import sys
def main():
    test_paper = [list(input().rstrip()) for _ in range(3*N)]
    for i in range(1, 3*N, 3):
        for j in range(0, 8*M, 8):
            k = 6+int(test_paper[i][j+6] != '.')
            if int(test_paper[i][j+1]) + int(test_paper[i][j+3]) == int(''.join(test_paper[i][j+5:j+k])):
                test_paper[i-1][j+1:j+k] = test_paper[i+1][j+1:j+k] = '*'*(k-1)
                test_paper[i][j] = test_paper[i][j+k] = '*'
            else: test_paper[i-1][j+3] = test_paper[i][j+2] = test_paper[i+1][j+1] = '/'

    print("\n".join(map(lambda x: "".join(x), test_paper)))
if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().split())
    main()