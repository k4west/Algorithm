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
        
            a = [row1[0], row2[0]] 
            b = [row1[1] + row2[0], row2[1] + row1[0]]
            
            for i in range(2, n):
                a, b = b, [row1[i] + max(b[1], a[1]), 
                           row2[i] + max(b[0], a[0])]
            li.append(max(b))
        
        else: li.append(max(int(input()), int(input())))
    print("\n".join(map(str, li)))

if __name__ == "__main__":
    main()