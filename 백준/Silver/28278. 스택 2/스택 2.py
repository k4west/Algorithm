def main():
    n = int(input())
    stack = []
    ans = []
    cnt = 0
    for _ in range(n):
        a, *b = map(int, input().split())
        if a == 1:
            stack.append(b[0])
            cnt += 1
        elif a == 2:
            if cnt:
                ans.append(stack.pop())
                cnt -= 1
            else:
                ans.append(-1)
        elif a == 3:
            ans.append(cnt)
        elif a == 4:
            ans.append(1-bool(cnt))
        elif a == 5:
            ans.append(stack[-1] if cnt else -1)
    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()
