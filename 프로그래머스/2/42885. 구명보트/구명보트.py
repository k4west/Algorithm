def solution(people, limit):
    people.sort()
    boat, s, e = 0, 0, len(people)-1
    while s <= e:
        if people[s] + people[e] <= limit:
            s += 1
            e -= 1
        else:
            e -= 1
        boat += 1        
    return boat