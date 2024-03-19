import sys
def main():
    a = -1000000
    for i in map(int, sys.stdin.readline().split()):
        if a > i:
            print('Bad')
            return
        a = i
    print('Good')
sys.exit(main())