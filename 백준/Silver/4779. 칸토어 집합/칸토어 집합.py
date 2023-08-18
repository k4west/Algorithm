a = [0 for _ in range(13)]
a[0] = '-'
for i in range(12):
    a[i + 1] = a[i] + " " * (3 ** i) + a[i]
while True:
    try:
        print(a[int(input())])
    except:
        break