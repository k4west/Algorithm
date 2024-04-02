a = open(0)
def main():
    for t in range(int(next(a))):
        d = {}
        for _ in range(int(next(a))):
            name_year = next(a).rstrip()
            name = name_year[:-5]
            year = name_year[-4:]
            if name in d: d[name].add(year)
            else: d[name] = {year}
        print("\n".join([f"Case #{t+1}:"] + sorted([name for name, years in d.items() if len(years) < 5])))
main()