a=[int(input()) for _ in range(int(input()))]
print("\n".join("ABCD"[((n-2)//3+1+((n-2)%3)%2)%4] for n in a))