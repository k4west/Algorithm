def solution(s, skip, index):
    sk = [ord(c)-97 for c in skip]
    li = []
    for c in s:
        n = ord(c)-97
        for _ in range(index):
            n = (n+1)%26
            while n in sk:
                n = (n+1)%26
        li.append(chr(n+97))
    return "".join(li)