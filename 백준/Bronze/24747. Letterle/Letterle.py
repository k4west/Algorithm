a = open(0)
letter = next(a).rstrip()
flag = False
for i, guess in enumerate(a):
    if letter == guess.rstrip():
        flag = True
        break
    else:
        tmp = ''
        for l, g in zip(letter, guess):
            if l == g: tmp += 'G'
            elif g in letter: tmp += 'Y'
            else: tmp += 'X'
        if i < 6: print(tmp)
        else: print('LOSER')
if flag:
    print("WINNER")