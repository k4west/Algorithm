for i in [*open(0)][1:]:
    s, t = i.split()
    print(f'Shifting {s} by {(t:=int(t))} positions gives us: {s[-t:]}{s[:-t]}')