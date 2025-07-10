paper = [[0 for _ in range(101)] for _ in range(101)]
for i in range(int(input())):
    i, j = map(int, input().split())
    for p in range(i, i+10):
        for q in range(j, j+10):
            paper[p][q] = 1
print(sum(sum(paper, [])))