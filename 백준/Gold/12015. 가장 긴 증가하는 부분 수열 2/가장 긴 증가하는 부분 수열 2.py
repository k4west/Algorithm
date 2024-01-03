import sys
input = sys.stdin.readline

def main():
    N = int(input())
    arr = tuple(map(int, input().split()))
    ans = [arr[0]]

    for a in arr[1:]:
        if a > ans[-1]: ans.append(a)
        else:
            s, e, t = 0, len(ans)-1, N
            while s <= e:
                m = (s+e)//2
                if ans[m] >= a: 
                    e = m-1
                    t = m
                else:
                    s = m+1
            if t!= N:
                ans[t] = a
    print(len(ans))

if __name__ == "__main__":
    main()