import sys
input = sys.stdin.readline
ans = []
while n := int(input()):
    d = {}
    for _ in range(n):
        A, a, _, b, B = input().rstrip().split()
        pa = pb = 1
        if (a := int(a)) < (b := int(b)): A, a, b, B = B, b, a, A
        if not A in d: d[A] = [0, 0]
        if not B in d: d[B] = [0, 0]
        if c := a - b: pa, pb = 3, 0
        d[A][0] += pa
        d[B][0] += pb
        d[A][1] += c
        d[B][1] -= c
    li = [[points, goal, name] for name, [points, goal] in d.items()]
    li.sort(key=lambda x: [-x[0], -x[1]])
    ans.append("\n".join(f"{x[0]} {x[2]}" for x in li))
print("\n\n".join(ans))