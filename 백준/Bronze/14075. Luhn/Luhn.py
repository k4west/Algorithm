s = 0
for i, j in enumerate(map(int, input())):
    if i%2==0: j*=2
    s += j%10+j//10
print('NDEA'[s%10==0::2])