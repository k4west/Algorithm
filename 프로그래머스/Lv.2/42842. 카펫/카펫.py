def solution(brown, yellow):
    B = (brown - 4) // 2
    for i in range(1, int(yellow**.5)+1):
        if yellow % i:
            continue
        if i + (q:= yellow // i) == B:
            return [q+2, i+2]