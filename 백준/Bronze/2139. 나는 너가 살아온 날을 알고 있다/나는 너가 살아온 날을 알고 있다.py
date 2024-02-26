import sys

days = {1:0,2:31,3:59,4:90,5:120,6:151,7:181,8:212,9:243,10:273,11:304,12:334}
input = lambda: map(int, sys.stdin.readline().split())
ans = []
yoon = 0
while True:
    d, m, y = input()
    if y == 0: break
    if (m > 2) and (y % 4 == 0):
        if y % 100 != 0 or y % 400 == 0:
            yoon = 1
    ans.append(d + days[m] + yoon)
    yoon = 0
print("\n".join(map(str, ans)))