def main():
    string = input()
    bomb = list(input())
    b = len(bomb)
    x = bomb[-1]

    stack = []
    for s in string:
        stack.append(s)
        if s == x and stack[-b:] == bomb:
            del stack[-b:]

    print("".join(stack) if stack else "FRULA")

if __name__ == "__main__":
    main()