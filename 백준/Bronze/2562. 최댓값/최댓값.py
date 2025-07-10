M = 0
for i in range(1, 10):
    n = int(input())
    if n > M:
        M = n
        idx = i
print(M, idx, sep='\n')