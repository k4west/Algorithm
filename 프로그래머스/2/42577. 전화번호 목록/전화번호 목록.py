def solution(phone_book):
    phone_book.sort()
    for i in range((n:= len(phone_book))-1):
        a, b = phone_book[i], phone_book[i+1]
        if b[0] != a[0]: continue
        if b[:len(a)] == a: return False
    return True