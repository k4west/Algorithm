import sys
def main():
    input = sys.stdin.readline
    ans = []
    i = 1
    while n:=int(input()):
        animals = {}
        for _ in range(n):
            animal = input().split()[-1].rstrip().lower()
            animals[animal] = animals.get(animal, 0) + 1
        animals = [f"{animal} | {num}" for animal, num in animals.items()]
        animals.sort()
        ans.append(f"List {i}:\n"+"\n".join(animals))
        i += 1
    print(*ans, sep="\n")
main()