def main():
    a = open(0)
    H, W = map(int, next(a).split())
    sky = [next(a).strip() for _ in range(H)]
    clouds = [[-1 for _ in range(W)] for _ in range(H)]
    
    for i in range(H):
        t = 0
        for j in range(W):
            if sky[i][j] == 'c':
                clouds[i][j] = 0
                t = 1
            elif t:
                clouds[i][j] = t
                t += 1
    
    print("\n".join(" ".join(map(str, i)) for i in clouds))

if __name__=="__main__":
    main()
