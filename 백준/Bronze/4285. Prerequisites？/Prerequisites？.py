import sys
def main():
    input = sys.stdin.readline
    ans = []
    while True:
        km = input().rstrip()
        if km == '0':
            break
        _, m = map(int, km.split())
        chosen = set(input().split())
        flag = True
        for _ in range(m):
            _, r, *courses = input().split()
            if flag and sum(course in chosen for course in courses) < int(r):
                flag = False
        ans.append("yes" if flag else "no")
    print("\n".join(ans))
main()