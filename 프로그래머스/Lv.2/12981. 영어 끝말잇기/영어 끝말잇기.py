def solution(n, words):
    last = words[0][-1]
    v = {words[0]}
    for i, word in enumerate(words[1:], 1):
        if word in v or last != word[0]:
            return [i%n+1, i//n+1]
        v.add(word)
        last = word[-1]
    return [0, 0]