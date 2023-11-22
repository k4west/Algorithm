def main():
    string = input()
    bomb = list(input())
    b = len(bomb)

    stack = []
    for s in string:
        stack.append(s)
        if stack[-b:] == bomb:
            del stack[-b:]

    print("".join(stack) if stack else "FRULA")

if __name__ == "__main__":
    main()