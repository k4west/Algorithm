ans = []
a = open(0)
for _ in range(int(next(a))):
    books = [next(a).strip() for _ in range(int(next(a)))]
    books.sort()

    for i, j in zip(books, books[1:]):
        if j.startswith(i):
            ans.append('NO')
            break
    else:
        ans.append('YES')

print('\n'.join(map(str, ans)))