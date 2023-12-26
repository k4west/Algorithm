import sys
input = sys.stdin.readline

def main():
    pitch = {0:'A', 2:'B', 3:'C', 5:'D', 7:'E', 8:'F', 10:'G'}
    keyboard = [True, False, True, True, False, True, False, True, True, False, True, False]
    arr = [int(input()) for _ in range(int(input()))]
    ans = []
    for i in pitch.keys():
        t, flag = i, False
        for j in arr:
            t = (t+j)%12
            if not keyboard[t]:
                flag = True
                break
        if flag:
            continue
        ans.append(" ".join((pitch[i], pitch[t])))
    print("\n".join(ans))

if __name__ == "__main__":
    main()