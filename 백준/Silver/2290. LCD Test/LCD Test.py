s, n = input().split()
s = int(s)
d = {"0": [' - ','| |','   ','| |',' - '], "1": ['   ','  |','   ','  |','   '], "2": [' - ','  |',' - ','|  ',' - '], "3": [' - ','  |',' - ','  |',' - '], "4": ['   ','| |',' - ','  |','   '], "5": [' - ','|  ',' - ','  |',' - '], "6": [' - ','|  ',' - ','| |',' - '], "7": [' - ','  |','   ','  |','   '], "8": [' - ','| |',' - ','| |',' - '], "9": [' - ','| |',' - ','  |',' - ']}
for c in "0123456789":
    for i in range(5): d[c][i] = d[c][i][0]+d[c][i][1]*s+d[c][i][2]
    d[c] = [d[c][0], *[d[c][1] for _ in range(s)], d[c][2], *[d[c][3] for _ in range(s)], d[c][4]]
print("\n".join(" ".join([''.join(d[k][i][j] for j in range(s+2)) for k in n]) for i in range(2*s+3)))