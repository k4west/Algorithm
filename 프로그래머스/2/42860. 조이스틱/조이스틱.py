def solution(name):
    n = len(name)
    move = n - 1
    while move > 0 and name[move] == 'A':
        move -= 1
    if move >= 0:
        ans = sum(min(ord(letter) - 65, 91 - ord(letter)) for letter in name)
        for i in range(n):
            j = i + 1
            while j < n and name[j] == 'A':
                j += 1
            move = min(move, 2*i + n - j, 2 * (n - j) + i)
        ans += move
    return ans
