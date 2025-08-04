def dfs(s):
    li[0] += s
    for i, child in enumerate(trees[s]):
        if i:
            li[1] += s
        if child != '.':
            dfs(child)
            li[2] += child


trees = {}
li = ['']*3
for _ in range(int(input())):
    parent, left, right = input().split()
    trees[parent] = (left, right)

dfs('A')
li[2] += 'A'
print('\n'.join(li))
