import sys
input = sys.stdin.readline

def main():
    N = int(input())
    # 지뢰 주위 8칸 이동 정보
    d = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    bomb = []
    ans = [[0]*N for _ in range(N)]
    
    for i in range(N):
        for j, k in enumerate(input().rstrip()):
            if k in '123456789':
                bomb.append((i, j, int(k)))  # 지뢰 위치 저장
                ans[i][j] = '*'  # 지뢰 표시
    
    for i, j, k in bomb:
        for di, dj in d:  # map 범위 내에서 지뢰 주위 8칸 탐색
            if 0 <= (ni:=i+di) < N and 0 <= (nj:=j+dj) < N:
                if (t:=ans[ni][nj]) !='*' and t != 'M':  # 지뢰나 10 이상이 아닌 경우
                    t += k  # 지뢰 수 더하기
                    if t >= 10:
                        ans[ni][nj] = 'M'  # 10 이상이면 'M'으로 표시
                    else: ans[ni][nj] = t
    
    print("\n".join("".join(map(str, row)) for row in ans))

if __name__ == "__main__":
    main()