def main():
    if (N:= int(input())) == 0:
        return 'NO'
    factorials = [1]
    for i in range(1, 21):
        factorials.append(factorials[-1]*i)
    for i in factorials[::-1]:
        if N >= i:
            N -= i
    if N: return 'NO'
    return 'YES'
    
print(main())