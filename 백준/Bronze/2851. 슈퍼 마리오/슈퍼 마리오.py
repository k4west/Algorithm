score = 0
for _ in range(10):
    t = int(input())
    if abs(100-score) >= abs(100-score-t):
        score += t
    else:
        break
print(score)
