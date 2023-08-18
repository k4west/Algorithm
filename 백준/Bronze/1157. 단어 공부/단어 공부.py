import sys
input = sys.stdin.readline

str1 = input().replace('\n', '').upper()
maxn = 0
for i in set(str1):
    count = str1.count(i)
    if maxn < count:
        maxn = count
        answer = [i]
    elif maxn == count:
        answer.append(i)
print('?' if len(answer) > 1 else answer[0])