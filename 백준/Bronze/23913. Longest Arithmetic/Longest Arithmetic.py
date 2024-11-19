a = open(0)
t = []
for i in range(int(next(a))):
    max_length = length = 2
    n = int(next(a))
    A = [*map(int, next(a).split())]
    diff = A[1] - A[0]
    prev = A[1]
    for now in A[2:]:
        if diff != (diff_:=now-prev):
            if max_length < length:
                max_length = length
            length = 2
            diff = diff_
        else:
            length += 1
        prev = now
    if max_length < length:
        max_length = length
    t.append(f"Case #{i+1}: {max_length}")
print("\n".join(t))