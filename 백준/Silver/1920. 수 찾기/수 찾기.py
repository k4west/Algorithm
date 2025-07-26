input()
A = set(map(int, input().split()))
input()
print("\n".join('1' if n in A else '0' for n in map(int, input().split())))