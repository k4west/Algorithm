d={4:[11],5:[17],6:[14],7:[12],8:[1],9:[7],10:[4],11:[2],12:[0],13:[8]}
n = int(input())
if 8<=n<=26:
    for i in d:
        if n-i in d:print(f'{d[i][0]:02d}:{d[n-i][0]:02d}');break
else:print('Impossible')