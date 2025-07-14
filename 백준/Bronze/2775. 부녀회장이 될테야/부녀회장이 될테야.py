answer = []
apt = [[i for i in range(15)]] + [[0 for _ in range(15)] for _ in range(15)]
for i in range(1, 15):
    for j in range(1, 15):
        apt[i][j] = apt[i-1][j] + apt[i][j-1]
for _ in range(int(input())):
    k = int(input())
    n = int(input())
    answer.append(apt[k][n])
print(*answer, sep='\n')