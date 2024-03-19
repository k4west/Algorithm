import sys
def main():
    a, *arr, = map(int, sys.stdin.readline().split())
    for b in arr:
        if a > b:
            print('Bad')
            return
        a = b
    print('Good')
main()