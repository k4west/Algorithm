H, M = list(map(int, input().split()))

if M < 45:
    M += 60
    if H != 0:
        H -= 1
    else:
        H = 23
M -= 45

print(H, M)