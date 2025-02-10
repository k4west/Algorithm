def main():
    a = open(0)
    N = int(next(a))
    tasks = []
    scores = 0
    for i in range(N):
        flag, *info = map(int, next(a).split())
        if flag:
            tasks.append(info)
        if not tasks:
            continue
        tasks[-1][1] -= 1
        if not tasks[-1][1]:
            score, _ = tasks.pop()
            scores += score
    print(scores)
main()