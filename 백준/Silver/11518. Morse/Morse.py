import sys

input = sys.stdin.readline
alpha2code = {}
code2alpha = {}
for _ in range(26):
    alpha, code = input().rstrip().split()
    alpha2code[alpha] = code
    code2alpha[code] = alpha
dictionary = {}
for _ in range(int(input())):
    word = input().rstrip()
    morse = "".join(alpha2code[w] for w in word)
    dictionary[morse] = word

ans = []
while n := int(input()):
    tmp = []
    flag = True
    for _ in range(n):
        if not flag:
            input()
            continue
        if (morse := input().rstrip()) in dictionary:
            tmp.append(dictionary[morse])
        else:
            tmp = [morse, "not in dictionary."]
            flag = False
    ans.append(" ".join(tmp))
print("\n".join(ans))