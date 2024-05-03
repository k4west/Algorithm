a = open(0)
letter = next(a).rstrip()
ans = []
flag = False
for guess in a:
    if letter == guess.rstrip():
        flag = True
        break
    else:
        tmp = ''
        for l, g in zip(letter, guess):
            if l == g:
                tmp += 'G'
            elif g in letter:
                tmp += 'Y'
            else:
                tmp += 'X'
        ans.append(tmp)
if flag:
    ans.append("WINNER")
else:
    ans[6] = 'LOSER'
print("\n".join(ans))