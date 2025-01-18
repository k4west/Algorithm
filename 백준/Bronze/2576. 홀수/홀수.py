odds = [i for i in map(int, open(0).read().split()) if i%2]
print(*[sum(odds), min(odds)] if odds else [-1], sep='\n')