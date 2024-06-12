input()
print(int("".join(sorted(input().split(), key=lambda x: x*9, reverse=True))))