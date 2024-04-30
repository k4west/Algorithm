a, b = map(int, input().split())
print(min(a, b) if (a*b)%2 else 0)