import sys

def main():
    input = sys.stdin.readline
    ans = []
    while True:
        km = list(map(int, input().split()))
        if km[0] == 0:
            break
        k, m = km
        chosen = set(map(int, input().split()))
        flag = 0
        for _ in range(m):
            cnt = 0
            _, r, *courses = list(map(int, input().split()))
            for course in courses:
                if course in chosen:
                    cnt += 1
            if cnt < r:
                flag = 1
        ans.append("yneos"[flag::2])
    print("\n".join(ans))
main()