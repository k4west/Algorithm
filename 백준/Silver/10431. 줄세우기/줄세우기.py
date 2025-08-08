ans = []
for _ in range(int(input())):
    T, *li, = map(int, input().split())

    cnt = 0
    stack = li[:1]
    for h in li[1:]:
        tmp = []
        while stack and stack[-1] > h:
            tmp.append(stack.pop())
            cnt += 1
        stack.append(h)
        while tmp:
            stack.append(tmp.pop())

    ans.append(f"{T} {cnt}")

print("\n".join(ans))
