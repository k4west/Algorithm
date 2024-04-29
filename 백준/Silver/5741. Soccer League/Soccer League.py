import sys

input = sys.stdin.readline

ans = []
while n := int(input()):
    d = {}
    for _ in range(n):
        A, a, _, b, B = input().rstrip().split()
        if (a := int(a)) < (b := int(b)):
            A, a, b, B = B, b, a, A
        if not A in d:
            d[A] = [0, 0]
        if not B in d:
            d[B] = [0, 0]
        if a != b:
            c = a - b
            d[A][0] += 3
            d[A][1] += c
            d[B][1] -= c
        else:
            d[A][0] += 1
            d[B][0] += 1
    li = [[points, goal, name] for name, [points, goal] in d.items()]
    li.sort(key=lambda x: [-x[0], -x[1]])
    ans.append("\n".join(f"{x[0]} {x[2]}" for x in li))
print("\n\n".join(ans))