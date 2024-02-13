def solution(k, dungeons):   
    def f(n, dungeons, d, ans):
        for i in range(n):
            tmp = d.copy()
            least, used = dungeons[i]
            for user in d:
                if user >= least:
                    tmp[user-used] = d.get(user, 0) + 1
            if n - 1:
                ans = f(n-1, dungeons[:i] + dungeons[i+1:], tmp, ans)
            else:
                for num in tmp.values():
                    if ans < num:
                        ans = num
        return ans
    
    return f(len(dungeons), dungeons, {k:0}, -1)