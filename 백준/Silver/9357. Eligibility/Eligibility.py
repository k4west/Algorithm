import sys
input = sys.stdin.readline
def main():
    for t in range(int(input())):
        d = {}
        for _ in range(int(input())):
            name_year = input().rstrip()
            name = name_year[:-5]
            year = name_year[-4:]
            if name in d: d[name].add(year)
            else: d[name] = {year}
        print("\n".join([f"Case #{t+1}:"] + sorted([name for name, years in d.items() if len(years) < 5])))
main()