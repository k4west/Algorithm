import sys
input = sys.stdin.readline

def main():
    ans = []
    for _ in range(int(input())):
        n = int(input())
        li = [0] + list(map(int, input().split()))
        d = [0]*(n+1)
        for i in li: d[i] += 1
        
        left = [i for i in range(1, n+1) if not d[i]]
        for i in left:
            d[(j:=li[i])] -= 1
            if not d[j]: left.append(j)
    
        ans.append(str(len(left)))
    print("\n".join(ans))

if __name__ == "__main__":
    main()