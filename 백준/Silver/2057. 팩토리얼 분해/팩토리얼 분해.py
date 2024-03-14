def main():
    if (N:= int(input())) == 0: return 'NO'
    dp = [1]
    for i in range(1, 21): dp.append(dp[-1]*i)
    for i in dp[::-1]:
        if N >= i: N -= i
    if N: return 'NO'
    return 'YES'
    
print(main())