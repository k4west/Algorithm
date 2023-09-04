def solution(babbling):
    count = 0
    check = ["aya", "ye", "woo", "ma"]
    for b in babbling:
        for c in check:
            if c in b:
                b = b.replace(c," ",1)
        if not b.split():
            count += 1
        print(b.split())
    return count