A, B, C = map(int, input().split())
n, m = (A+B)%C, (A*B)%C
print(f"{n}\n{n}\n{m}\n{m}")