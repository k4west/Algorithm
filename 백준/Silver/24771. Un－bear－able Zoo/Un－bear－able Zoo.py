import sys
input = sys.stdin.readline
ans = []
i = 1
while n:=int(input()):
    animals = {}
    for _ in range(n):
        animal = input().split()[-1].rstrip().lower()
        animals[animal] = animals.get(animal, 0) + 1
    ans.append(f"List {i}:\n"+"\n".join(sorted([f"{animal} | {num}" for animal, num in animals.items()])))
    i += 1
print(*ans, sep="\n")