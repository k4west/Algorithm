def main():
    i = open(0)
    for _ in range(int(next(i))):
        a, b, s = next(i).split()
        o = (int(a)*60 + round((float(s[3:]) - 8) * 60) + int(b)) % 1440
        print(f"{o//60%24:02d}:{o%60:02d}")
main()