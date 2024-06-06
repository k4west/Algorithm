s=set('RB')
def main():
    n=int(input());a=input();r=t=1
    for i in range(n-1):
        if set(a[i:i+2])==s:t+=1
        else:r=max(r,t);t=1
    print(max(r,t))
main()