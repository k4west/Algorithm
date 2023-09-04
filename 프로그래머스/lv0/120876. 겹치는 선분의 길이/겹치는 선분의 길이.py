def solution(lines):
    li = ['0']*200
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            s = 100 + max(lines[i][0], lines[j][0])
            e = 100 + min(lines[i][1], lines[j][1])
            if e > s:
                li[s:e] = ['1'] * (e - s)
    return "".join(li).count('1')