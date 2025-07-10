S = input()
li = [-1 for _ in range(26)]
for i, s in enumerate(S):
    if li[(j:=ord(s)-97)] == -1:
        li[j] = i
print(*li)