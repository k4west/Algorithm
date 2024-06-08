def main():
    li = [1, 1]
    for _ in range(int(input())-1):li[0],li[1]=li[1],(li[1]+li[0]*2)%10007
    print(li[1])
main()