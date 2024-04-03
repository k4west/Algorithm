n = max(len(a:=input()), len(b:=input()))
print("".join(['0' if (x<=2 and y<=2) or (x>=7 and y>=7) else '9' for x, y in map(lambda x: map(int, x), zip(a.zfill(n), b.zfill(n)))]))