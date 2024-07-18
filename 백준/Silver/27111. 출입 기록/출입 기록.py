def main():
    _, *a = open(0)
    visit = {}
    c = 0
    for i in a:
        idx, state = i.split()
        state = state.strip()
        if state == '1':
            if idx in visit:
                c += 1
            else:
                visit[idx] = ''
        else:
            if idx in visit:
                del visit[idx]
            else:
                c += 1
    print(c + len(visit))
main()