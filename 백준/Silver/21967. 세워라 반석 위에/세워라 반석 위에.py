import sys
def main():
    input = sys.stdin.readline
    nums = [0] * 11
    s = ans = tmp = 0
    input()
    arr = list(map(int, input().split()))
    for a in arr:
        nums[a] += 1
        tmp += 1
        li = [i for i, j in enumerate(nums) if j]
        if li[-1] - li[0] > 2:
            nums[arr[s]] -= 1
            tmp -= 1
            s += 1
        if ans < tmp:
            ans = tmp
    print(ans)
main()