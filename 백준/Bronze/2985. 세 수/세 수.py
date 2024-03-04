a, b, c = input().split()
for op in "+-*/":
    if eval(f"{a}{op}{b}=={c}"): print(f"{a}{op}{b}={c}"); break
    if eval(f"{a}=={b}{op}{c}"): print(f"{a}={b}{op}{c}"); break