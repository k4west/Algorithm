def f(i, s):
    global score

    if i == 10:
        a, b = abs(score - 100), abs(s - 100)
        if a > b or a == b and score < s:
            score = s
        return

    f(10, s)
    f(i+1, s+mush[i])


score = 0
*mush, = map(int, (input() for _ in range(10)))

f(0, 0)
print(score)
