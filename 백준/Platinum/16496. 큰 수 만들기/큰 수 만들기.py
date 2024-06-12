from functools import cmp_to_key as ck
input()
def main():print(int("".join(sorted(input().split(),key=ck(lambda x,y:2*(x+y>y+x)-1))[::-1])))
main()