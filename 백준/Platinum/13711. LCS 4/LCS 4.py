import sys
def main():
    input = sys.stdin.readline
    n = int(input())
    n1 = list(map(int, input().split()))
    n2 = list(map(int, input().split()))

    n1_idx = [0] * (n+1)
    for i in range(n):
        n1_idx[n1[i]] = i+1 # n1의 숫자 순서를 dp에 저장

    ans = [n1_idx[n2[0]]]
    for num in n2[1:]:
        idx = n1_idx[num]
        if ans[-1] < idx:
            ans.append(idx)
        else:
            s = 0
            e = len(ans)
            while s < e:
                m = (s + e) // 2
                if ans[m] < idx:
                    s = m + 1
                else:
                    e = m
            ans[s] = idx

    print(len(ans))
main()