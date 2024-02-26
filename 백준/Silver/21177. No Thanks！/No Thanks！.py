import sys

input = sys.stdin.readline
_ = input()
cards = sorted(map(int, input().split()))
score = 0
prev = -1

for num in cards:
    if prev + 1 != num:
        score += num
    prev = num
print(score)