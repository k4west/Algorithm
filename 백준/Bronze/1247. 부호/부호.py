import io, os, sys
def main():
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    ans = []
    for _ in range(3):
        s = sum(int(input()) for _ in range(int(input())))
        if s > 0: ans.append("+")
        elif s < 0: ans.append("-")
        else: ans.append("0")
    print("\n".join(ans))
if __name__ == "__main__":
    sys.exit(main())