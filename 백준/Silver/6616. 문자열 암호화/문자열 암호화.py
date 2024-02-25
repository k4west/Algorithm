import sys

input = sys.stdin.readline
ans = []
while True:
    if (n := int(input())) == 0:
        break
    message = "".join(input().rstrip().split()).upper()
    tmp, i, j, length = {}, 0, 0, len(message)
    for k in range(length):
        tmp[i] = message[k]
        i += n
        if i >= length:
            i = (j := j + 1)
    ans.append("".join(map(lambda x: x[1], sorted(tmp.items(), key=lambda x: x[0]))))
print("\n".join(ans))