import sys

input = lambda: map(int, sys.stdin.readline().split())
ans = []
while True:
    A, B, C = input()
    if not A:
        break

    if A == B == C:  # set
        if A == 13:
            ans.append("*")
        else:
            ans.append(f'{A+1} {A+1} {A+1}')

    elif A == B or B == C or C == A:  # pair
        unmatched = A ^ B ^ C
        pair = A
        if pair == unmatched:
            pair = B
        if pair == 13 and unmatched == 12:
            ans.append("1 1 1")
        elif unmatched == 13:
            ans.append(" ".join(map(str, sorted((1, pair + 1, pair + 1)))))
        else:
            t = 1
            if unmatched + 1 == pair:
                t += 1
            ans.append(" ".join(map(str, sorted((unmatched + t, pair, pair)))))

    else:  # not piar
        ans.append("1 1 2")

print("\n".join(ans))