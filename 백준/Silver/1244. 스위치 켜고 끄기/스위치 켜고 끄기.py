N = int(input())
switch = [*map(int, input().split())]
for _ in range(int(input())):
    gender, num = map(int, input().split())
    if gender == 1:
        for i in range(num-1, N, num):
            switch[i] ^= 1
    else:
        t = 0
        for i in range(1, min(num, N-num+1)):
            if switch[num-i-1] != switch[num+i-1]:
                break
            t = i
        for i in range(num-t-1, num+t):
            switch[i] ^= 1
print('\n'.join(' '.join(map(str, switch[20*i:20*(i+1)])) for i in range(N//20+bool(N%20))))