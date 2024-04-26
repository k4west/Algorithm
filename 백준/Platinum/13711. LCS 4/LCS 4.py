import sys
input = sys.stdin.readline
n = int(input())
n1 = list(map(int, input().split()))
n2 = list(map(int, input().split()))

n1_idx = [0] * (n)
for i in range(n):
    n1_idx[n1[i] - 1] = i # n1의 숫자 순서를 dp에 저장
n2_idx_in_n1 = [n1_idx[n2[i] - 1] for i in range(n)] # n2의 숫자가 n1에서 몇번째 인덱스에 해당하는지 저장

ans = [n2_idx_in_n1[0]]
for num in n2_idx_in_n1[1:]:
    if ans[-1] < num:
        ans.append(num)
    else:
        s = 0
        e = len(ans)
        while s < e:
            m = (s + e) // 2
            if ans[m] < num:
                s = m + 1
            else:
                e = m
        ans[s] = num

print(len(ans))