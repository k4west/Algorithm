import sys

input = lambda: sys.stdin.readline().rstrip().split()
ans = []
while True:
    s = input()
    if s[0] == "#":
        break
    target, guess = map(list, s)
    org = "".join(guess)
    result = [0, 0, 0]
    N = len(target)
    for i, (j, k) in enumerate(zip(target, guess)):
        if j == k:
            result[0] += 1
            target[i] = guess[i] = False
    for i in range(N):
        if guess[i]:
            if i > 0 and target[i - 1] == guess[i]:
                result[1] += 1
                target[i - 1] = guess[i] = False
            elif i < N - 1 and target[i + 1] == guess[i]:
                result[1] += 1
                target[i + 1] = guess[i] = False
    for i in range(N):
        if j := guess[i]:
            if j in target:
                result[2] += 1
                target[target.index(j)] = False
    ans.append(f"{org}: {result[0]} black, {result[1]} grey, {result[2]} white")
print("\n".join(ans))