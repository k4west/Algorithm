N = int(input())
li = [int(input()) for _ in range(N)]
stack = []
idx = 0
ans = []

# 숫자를 오름차순으로 stack에 push하는데
# 수열을 만들기 위해서 pop해야하는 원소이면, pop하고
# 이후에 stack에 pop할 수 있는 원소인지 확인(while)
for i in range(1, N+1):
    if i == li[idx]:
        ans.append('+')
        ans.append('-')
        idx += 1
        while stack and idx < N and stack[-1] == li[idx]:
            ans.append('-')
            stack.pop()
            idx += 1
    else:
        ans.append('+')
        stack.append(i)

# stack에 남아 있으면, 수열을 못 만드는 상황임
print('\n'.join(ans) if not stack else 'NO')