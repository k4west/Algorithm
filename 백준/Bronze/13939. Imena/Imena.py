int(input())
ss = input().replace("?", ".").replace("!", ".").split(".")
for s in ss:
    if s:
        s = s.replace(".", "")
        cnt = 0
        for t in s.split():
            t = t.strip()
            if t.isalpha() and t[0] == t[0].upper() and t[1:] == t[1:].lower():
                cnt += 1
        print(cnt)