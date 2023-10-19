from sys import stdin
input = stdin.readline

def main():
    T = int(input())
    li = []
    for _ in range(T):
        n = int(input())
        
        if n > 1:
            row1 = list(map(int, input().split()))
            row2 = list(map(int, input().split()))
        
            ans = [[row1[0], row2[0]], 
                [row1[1] + row2[0], row2[1] + row1[0]]]
            
            for i in range(2, n):
                ans = [ans[1], 
                    [row1[i] + max(ans[1][1], ans[0][1]), 
                        row2[i] + max(ans[1][0], ans[0][0])]]

            li.append(max(ans[1]))
        
        else:
            li.append(max(int(input()), int(input())))

    print("\n".join(map(str, li)))

if __name__ == "__main__":
    main()