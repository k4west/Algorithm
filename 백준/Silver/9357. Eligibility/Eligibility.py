for t in range(int(input())):
    d = {}
    contestants = []
    for _ in range(int(input())):
        name_year = input()
        name = name_year[:-5]
        year = name_year[-4:]

        if name in d:
            d[name].add(year)
        else:
            d[name] = {year}
    for name, years in d.items():
        if len(years) < 5:
            contestants.append(name)
    print(f"Case #{t+1}:")
    for name in sorted(contestants):
        print(name)