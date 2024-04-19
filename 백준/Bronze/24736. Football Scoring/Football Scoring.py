s = [6, 3, 2, 1, 2]
print(sum(a*b for a, b in zip(s, map(int, input().split()))), sum(a*b for a, b in zip(s, map(int, input().split()))))