from sys import stdin

def f(li: tuple) -> str:
    major, count = "", 0
    for n in li:
        if count == 0: major, count = n, 1
        elif major == n: count += 1
        else: count -= 1
    return major

def main() -> None:
    for _ in range(int(input())):
        t, *li = input().rstrip().split()
        if li.count(major := f(tuple(li))) > int(t) // 2: ans.append(major)
        else: ans.append(ing)
    print("\n".join(ans))

if __name__ == "__main__":
    input = stdin.readline
    ans, ing = [], "SYJKGW"
    main()