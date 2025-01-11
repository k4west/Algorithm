def composite(n):
    nums = [0,0,0] + [2*(i%2) for i in range(2, n)]
    for i in range(3, int(n**.5)+1):
        if not nums[i]:
            for j in range(i*i, n+1, i):
                if not nums[j]:
                    nums[j] = i
    return nums
    
def main():
    ans = []
    for k in map(int, open(0).read().split()[1:]):
        tmp = []
        idx = 0
        while (p:=composites[k]):
            tmp.append(p)
            k //= p
        ans.append(' '.join(map(str, tmp+[k])))
    print('\n'.join(ans))

composites = composite(5_000_000)
main()
