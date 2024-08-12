_,a=open(0)
dp=[0]
for i in map(int,a.split()):
    if dp[-1] < i:
        dp.append(i)
    else:
        for j, k in enumerate(dp[::-1]):
            if i > k:
                dp[-j] = i
                break
print(len(dp)-1)