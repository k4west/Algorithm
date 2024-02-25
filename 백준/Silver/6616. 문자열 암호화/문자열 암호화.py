import sys

input = sys.stdin.readline
ans = []
while True:
    if (n := int(input())) == 0: break
    message = "".join(input().rstrip().split()).upper()
    i, j, length = 0, 0, len(message)
    tmp = [""] * length
    for k in range(length):
        tmp[i] = message[k]; i += n
        if i >= length: i = (j := j + 1)
    ans.append("".join(tmp))
print("\n".join(ans))