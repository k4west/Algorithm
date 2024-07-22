c, _, *arr = map(int, open(0).read().split())
print(["No", "Yes"][c == sum((a*b for a, b in zip(arr[::2], arr[1::2])))])