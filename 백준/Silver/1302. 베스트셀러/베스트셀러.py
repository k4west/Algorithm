import sys
input = sys.stdin.readline

def main():
    N = int(input())
    books = {}
    for _ in range(N):
        title = input().rstrip()
        books[title] = books.get(title, 0) + 1

    m = 0
    for title, count in sorted(books.items()):
        if m < count:
            m = count
            ans = title
    print(ans)
    
if __name__ == "__main__":
    main()