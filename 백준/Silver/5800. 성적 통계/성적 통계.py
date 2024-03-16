ans = []
for i in range(1, int(input()) + 1):
    max_diff = 0
    n, *ss = map(int, input().split())
    ss.sort()
    for j in range(n - 1):
        if max_diff < (diff := ss[j + 1] - ss[j]):
            max_diff = diff
    ans.append(f"Class {i}\nMax {ss[-1]}, Min {ss[0]}, Largest gap {max_diff}")
print("\n".join(ans))