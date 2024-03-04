ans = []
for n in map(int, open(0)):
    check = set(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"))
    k, n_ = 1, n
    while True:
        check -= set(str(n_))
        if check: n_ += n; k += 1; continue
        ans.append(k); break
print('\n'.join(map(str, ans)))