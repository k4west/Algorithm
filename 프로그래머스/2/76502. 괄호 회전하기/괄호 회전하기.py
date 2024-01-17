def solution(s):
    d = {
        "(": (0, 1),
        ")": (0, -1),
        "[": (1, 1),
        "]": (1, -1),
        "{": (2, 1),
        "}": (2, -1),
    }
    li = [0, 0, 0]
    ans = 0
    flag = False
    n = len(s)
    t = {"(": ")", "[": "]", "{": "}"}
    stack = []

    for i in range(n):
        for j in range(n):
            if (b := s[(j + i) % n]) in t:
                stack.append(b)
            else:
                if not stack or t[stack.pop()] != b:
                    stack = []
                    break
        else:
            if not stack:
                flag = True
                break
        stack = []

    if flag:
        for j in range(n):
            k, v = d[s[(j + i) % n]]
            li[k] += v
            if li[0] == li[1] == li[2] == 0:
                ans += 1

    return ans